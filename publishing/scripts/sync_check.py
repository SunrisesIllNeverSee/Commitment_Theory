#!/usr/bin/env python3
"""Drift detector across DEPOSITS.md, DataCite, ORCID, and OpenAIRE.

Reads DEPOSITS.md as the local source of truth. Pulls live state from public,
auth-free APIs. Reports gaps, mismatches, duplicates, and missing ORCID
auto-sync events as a markdown report.

Usage:
    python3 sync_check.py
    python3 sync_check.py --report report.md
    python3 sync_check.py --skip-orcid --skip-openaire

Pure stdlib. No API keys. All read-only. Designed to live equally well in
publishing/scripts/ today or Publishing_Hub/automation/ tomorrow — paths are
resolved relative to this file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ORCID_ID = "0009-0002-9904-5390"

SCRIPT_DIR = Path(__file__).resolve().parent
PUBLISHING_DIR = SCRIPT_DIR.parent
DEPOSITS_MD = PUBLISHING_DIR / "DEPOSITS.md"


@dataclass
class Work:
    doi: str
    title: str
    version: str | None
    work_type: str | None
    registered: str | None  # YYYY-MM-DD
    source: str

    @property
    def normalized_doi(self) -> str:
        return self.doi.lower().strip()


def http_get_json(url: str, accept: str = "application/json") -> dict:
    req = urllib.request.Request(
        url,
        headers={"Accept": accept, "User-Agent": "publishing-sync/0.1"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_datacite_works(orcid: str) -> list[Work]:
    query = f"creators.nameIdentifiers.nameIdentifier:{orcid}"
    url = (
        "https://api.datacite.org/dois?"
        f"query={urllib.parse.quote(query)}&page[size]=100"
    )
    data = http_get_json(url)
    out: list[Work] = []
    for item in data.get("data", []):
        attrs = item.get("attributes", {})
        titles = attrs.get("titles") or [{}]
        out.append(
            Work(
                doi=(attrs.get("doi") or "").lower(),
                title=(titles[0] or {}).get("title", ""),
                version=attrs.get("version"),
                work_type=(attrs.get("types") or {}).get("resourceTypeGeneral"),
                registered=(attrs.get("registered") or "")[:10] or None,
                source="datacite",
            )
        )
    return out


def fetch_orcid_works(orcid: str) -> list[Work]:
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    data = http_get_json(url)
    out: list[Work] = []
    for group in data.get("group", []):
        summaries = group.get("work-summary") or []
        if not summaries:
            continue
        summary = summaries[0]
        external_ids = (summary.get("external-ids") or {}).get("external-id", [])
        doi = next(
            (e["external-id-value"] for e in external_ids if e.get("external-id-type") == "doi"),
            None,
        )
        if not doi:
            continue
        title = (((summary.get("title") or {}).get("title") or {}).get("value")) or ""
        registered = None
        pub = summary.get("publication-date") or {}
        if pub:
            y = (pub.get("year") or {}).get("value")
            m = (pub.get("month") or {}).get("value")
            d = (pub.get("day") or {}).get("value")
            registered = "-".join(p for p in [y, m, d] if p) or None
        out.append(
            Work(
                doi=doi.lower(),
                title=title,
                version=None,
                work_type=summary.get("type"),
                registered=registered,
                source="orcid",
            )
        )
    return out


def fetch_openaire_works(orcid: str) -> list[Work]:
    url = (
        "https://api.openaire.eu/search/publications?"
        f"orcid={orcid}&format=json&size=100"
    )
    data = http_get_json(url)
    out: list[Work] = []
    results = (((data.get("response") or {}).get("results") or {}).get("result") or [])
    for r in results:
        meta = ((((r.get("metadata") or {}).get("oaf:entity") or {}).get("oaf:result")) or {})
        pids = meta.get("pid") or []
        if isinstance(pids, dict):
            pids = [pids]
        doi = None
        for p in pids:
            if isinstance(p, dict) and p.get("@classid") == "doi":
                doi = (p.get("$") or "").lower()
                break
        if not doi:
            continue
        title = ""
        titles = meta.get("title") or []
        if isinstance(titles, dict):
            titles = [titles]
        if titles and isinstance(titles[0], dict):
            title = titles[0].get("$") or ""
        out.append(
            Work(
                doi=doi,
                title=title,
                version=None,
                work_type=None,
                registered=None,
                source="openaire",
            )
        )
    return out


DOI_RE = re.compile(r"10\.\d{4,9}/[\w.\-/]+", re.IGNORECASE)


def parse_local_dois(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text()
    return {m.group(0).lower().rstrip(".,)") for m in DOI_RE.finditer(text)}


def render_report(
    local: set[str],
    datacite: list[Work],
    orcid: list[Work],
    openaire: list[Work],
) -> str:
    by_doi_dc = {w.normalized_doi: w for w in datacite}
    by_doi_or = {w.normalized_doi: w for w in orcid}
    by_doi_oa = {w.normalized_doi: w for w in openaire}

    on_datacite = set(by_doi_dc)
    on_orcid = set(by_doi_or)
    on_openaire = set(by_doi_oa)

    missing_from_local = sorted(on_datacite - local)
    missing_from_orcid = sorted(on_datacite - on_orcid) if orcid else []
    missing_from_openaire = sorted(on_datacite - on_openaire) if openaire else []
    stale_in_local = sorted(local - on_datacite)

    duplicates: dict[str, list[Work]] = {}
    for w in datacite:
        key = (w.title or "").strip().lower()
        if key:
            duplicates.setdefault(key, []).append(w)
    duplicate_groups = {t: ws for t, ws in duplicates.items() if len(ws) > 1}

    lines: list[str] = []
    lines.append("# Publishing Sync Report")
    lines.append("")
    lines.append(f"- ORCID iD: `{ORCID_ID}`")
    lines.append(f"- DataCite works: **{len(on_datacite)}**")
    lines.append(f"- ORCID works: **{len(on_orcid) if orcid else 'skipped'}**")
    lines.append(f"- OpenAIRE works: **{len(on_openaire) if openaire else 'skipped'}**")
    lines.append(f"- DOIs in DEPOSITS.md: **{len(local)}**")
    lines.append("")

    lines.append("## DataCite works missing from DEPOSITS.md")
    if not missing_from_local:
        lines.append("_None — local ledger captures every live deposit._")
    else:
        for doi in missing_from_local:
            w = by_doi_dc[doi]
            lines.append(f"- `{doi}` — {w.title} (v {w.version or '-'}, {w.registered or '-'})")
    lines.append("")

    lines.append("## DOIs in DEPOSITS.md but NOT on DataCite")
    if not stale_in_local:
        lines.append("_None._")
    else:
        for doi in stale_in_local:
            lines.append(f"- `{doi}` — investigate (typo, retracted, or non-DataCite registrar)")
    lines.append("")

    if orcid:
        lines.append("## DataCite works missing from ORCID (auto-push gap)")
        if not missing_from_orcid:
            lines.append("_None — DataCite Auto-Update is keeping ORCID in sync._")
        else:
            for doi in missing_from_orcid:
                w = by_doi_dc[doi]
                lines.append(f"- `{doi}` — {w.title}")
            lines.append("")
            lines.append("> Fix: ORCID → Account Settings → confirm DataCite Auto-Update is on, or claim manually.")
        lines.append("")

    if openaire:
        lines.append("## DataCite works missing from OpenAIRE (harvester lag)")
        if not missing_from_openaire:
            lines.append("_None._")
        else:
            for doi in missing_from_openaire:
                w = by_doi_dc[doi]
                lines.append(f"- `{doi}` — {w.title}")
            lines.append("")
            lines.append("> OpenAIRE harvests Zenodo on a delay (days–weeks). Re-check next run.")
        lines.append("")

    lines.append("## Possible duplicate deposits (same title, multiple DOIs)")
    if not duplicate_groups:
        lines.append("_None detected._")
    else:
        for _, ws in duplicate_groups.items():
            lines.append(f"- **{ws[0].title}**")
            for w in sorted(ws, key=lambda x: x.registered or ""):
                lines.append(f"  - `{w.doi}` (v {w.version or '-'}, {w.registered or '-'})")
    lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report", type=Path, help="Write markdown report to this path (default: stdout)")
    p.add_argument("--skip-orcid", action="store_true")
    p.add_argument("--skip-openaire", action="store_true")
    args = p.parse_args(argv)

    print(f"[sync_check] Reading {DEPOSITS_MD}", file=sys.stderr)
    local = parse_local_dois(DEPOSITS_MD)
    print(f"[sync_check] Found {len(local)} DOI(s) locally", file=sys.stderr)

    print("[sync_check] Querying DataCite...", file=sys.stderr)
    datacite = fetch_datacite_works(ORCID_ID)
    print(f"[sync_check] DataCite returned {len(datacite)} work(s)", file=sys.stderr)

    orcid_works: list[Work] = []
    if not args.skip_orcid:
        print("[sync_check] Querying ORCID public API...", file=sys.stderr)
        try:
            orcid_works = fetch_orcid_works(ORCID_ID)
            print(f"[sync_check] ORCID returned {len(orcid_works)} work(s)", file=sys.stderr)
        except Exception as e:
            print(f"[sync_check] ORCID query failed: {e}", file=sys.stderr)

    openaire: list[Work] = []
    if not args.skip_openaire:
        print("[sync_check] Querying OpenAIRE...", file=sys.stderr)
        try:
            openaire = fetch_openaire_works(ORCID_ID)
            print(f"[sync_check] OpenAIRE returned {len(openaire)} work(s)", file=sys.stderr)
        except Exception as e:
            print(f"[sync_check] OpenAIRE query failed: {e}", file=sys.stderr)

    report = render_report(local, datacite, orcid_works, openaire)

    if args.report:
        args.report.write_text(report)
        print(f"[sync_check] Report written to {args.report}", file=sys.stderr)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())

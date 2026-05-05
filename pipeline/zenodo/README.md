# Zenodo Deposit Packages

Four papers packaged for deposit. Each folder is self-contained with the paper text, metadata, and a deposit checklist.

## Status

| Package | Status | Action |
|---------|--------|--------|
| [P-000_Prospectus/](P-000_Prospectus/) | **READY FOR DEPOSIT** | Run checklist → generate PDF → upload to Zenodo |
| [Paper-0_Conservation-Law/](Paper-0_Conservation-Law/) | LIVE (v.05) | Reference only — already on Zenodo |
| [L-000_Legal-Propositions/](L-000_Legal-Propositions/) | **NEEDS CCT→CT** | Rename → format → deposit to SSRN + Zenodo |
| [L-001_SLRO/](L-001_SLRO/) | FROZEN (60 days) | Placeholder — do not upload until ~July 1, 2026 |

## Deposit Order

1. **P-000** first (citation root for everything)
2. **L-000** second (citation root for legal track; cites P-000)
3. **Paper 0 v.06** later (after P-000 DOI exists to reference)
4. **L-001** after freeze lifts

## Zenodo Upload Workflow

1. Open each folder's `README_DEPOSIT.md` for metadata fields
2. Complete any remaining checklist items
3. Generate PDF from markdown/LaTeX source
4. Upload to Zenodo → mint DOI
5. Update downstream papers with new DOI reference

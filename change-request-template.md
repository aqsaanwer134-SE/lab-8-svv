# Change Request (CR) Template

## Theory
Once an artifact is baselined it must not be edited casually. A change request records
what is to change, why, what it affects and who approved it, so every change is
traceable and its impact is understood before work starts.

## Template
| Field | Entry |
|---|---|
| **CR ID** | CR-YYYY-NNN |
| **Date raised** | DD/MM/YYYY |
| **Raised by** | Name / Roll No |
| **Artifact** | File, version and item (e.g. `PSVS-REQ-v1.0`, S7) |
| **Current text** | Existing wording |
| **Proposed change** | Exact new wording |
| **Reason** | Defect ID(s) and justification |
| **Impact** | Affected requirements, later models/proofs/tests, effort, risk |
| **Approver** | Name / role |
| **Decision** | Approved / Rejected / Deferred |
| **Decision date** | DD/MM/YYYY |
| **New baseline** | Tag after implementation (e.g. `baseline-2`) |

## Example (filled in)
| Field | Entry |
|---|---|
| CR ID | CR-2026-001 |
| Date raised | 28/10/2026 |
| Raised by | <Your Name> / <RollNo> |
| Artifact | PSVS-REQ-v1.0, S7 |
| Current text | "Chamber temperature shall never rise above -18°C." |
| Proposed change | "Chamber temperature shall not exceed -18°C except during an authorised maintenance window (S8), with all boxes relocated beforehand." |
| Reason | D14: S7 contradicts S8 |
| Impact | S6, S8, and any later temperature constraint and proofs; low effort, low risk |
| Approver | Course Instructor |
| Decision | Pending |
| New baseline | baseline-2 |

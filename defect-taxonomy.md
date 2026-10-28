
# Defect Taxonomy for Requirements Inspection

## Theory
A defect taxonomy is a classification scheme that tells reviewers what kinds of problems
to look for. Using fixed categories makes inspection systematic, makes logs comparable
between reviewers, and allows defects to be counted and analysed. The eight required
categories are listed below, plus one extra category (Inconsistent terminology) that
was needed for PSVS.

## Taxonomy

| # | Category | Definition | Example (PSVS) |
|---|---|---|---|
| 1 | Ambiguity | A statement can be read in more than one valid way. | S10: "20% per year". Calendar or rolling year? 20% of which count? |
| 2 | Vagueness | Imprecise terms with no measurable meaning. | S2: "a large number of boxes". |
| 3 | Incompleteness | Required information, case or behaviour is missing. | S3: nothing says what happens when a chamber is full. |
| 4 | Contradiction | Two requirements cannot both be satisfied. | S7 (never above -18°C) vs S8 (warm to 0°C). |
| 5 | Non-verifiability | No objective test or measure can show the requirement is met. | S12: "good audit trail". |
| 6 | Redundancy | The same thing is stated more than once, risking divergence. | S6 "safe temperature" is made concrete by S7. |
| 7 | Infeasibility | Cannot be achieved with realistic technology or resources. | S7: "never" above -18°C, even in a total power failure. |
| 8 | Untraceability | No link to source, rationale, design or test. | No requirement has a rationale, owner or test reference. |
| 9 | Inconsistent terminology | One concept has several names, or one name several meanings. | "withdraw" (S4, S10, S11) vs "release" (S5). |

## Severity scale
| Severity | Meaning |
|---|---|
| Critical | Makes the system unsafe, insecure or impossible to build correctly. |
| High | Likely to cause wrong design or failed verification. |
| Medium | Causes confusion or rework but has a workable interpretation. |
| Low | Style or maintainability issue. |

# lab-8-svv
**Course:** Software Verification & Validation (Lab)
**Student:** <Aqsa>  **Roll No:** <sp24/BSSE090/B>

The Polar Seed Vault System (PSVS) stores sealed boxes of crop seeds deposited by registered institutions (gene banks, universities, governments).
## Overview
The Polar Seed Vault System (PSVS) stores sealed boxes of crop seeds deposited by
registered institutions (gene banks, universities, governments). Each box holds one
species. The vault is a custodian, not an owner. This repository contains the
requirements baseline and the defect analysis of the informal requirements S1-S12.

## Theory
**Verification and Validation (V&V).** Verification asks "are we building the system
right?", while validation asks "are we building the right system?". Errors in
requirements are the cheapest to fix and the most expensive to ignore, so requirements
are inspected before any design or code is written.

**Requirements inspection.** Each requirement is read critically and checked against a
defect taxonomy (ambiguity, vagueness, incompleteness, contradiction and so on). Every
defect is logged with evidence, severity and a suggested fix, so that it can be tracked
until resolved.

**Configuration management (CM).** CM keeps work products under control. A *baseline* is
a reviewed, frozen version of an artifact (here, tag `baseline-1`). Work is done on
*branches* and merged into `main` only after review. Any change to a baselined artifact
goes through a *change request* (ID, artifact, reason, impact, approver).



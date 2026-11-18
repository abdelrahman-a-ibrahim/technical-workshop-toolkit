# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
A toolkit for authoring and delivering practical workshops in Python, cloud engineering and Git collaboration. It organizes prerequisites, runnable examples, assessment rubrics, instructor guidance and accessible participant materials into a versioned delivery package.

## Target capabilities
- Define learner personas, prerequisites and observable outcomes. Build a diagnostic exercise that separates syntax gaps from systems reasoning.
- Create a Python debugging workshop with a broken example, instructor solution boundaries and a rubric; cover API validation and authorization failure cases.
- Create an AWS event development environment using synthetic data and an offline path. Teach retries, idempotency and resource cleanup; identify what requires a real cloud account.
- Create a Git simulation with feature branches, a conflict, a revert and a review checklist. Keep all history and collaborators fictional.
- Pilot with a self-review or consenting learner; label the evidence accurately. Add accessible handouts, transcripts, formative checks and a revision log.

## Acceptance criteria
- Each learning outcome maps to an exercise and an observable rubric criterion.
- Instructor guidance explains common misconceptions and gives graduated hints.
- Cloud cleanup and local alternatives are explicit.
- Feedback or outcome claims distinguish self-review from actual learner evidence.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.

# Technical Teaching Studio

**Turn engineering experiments into assessable learning**

> Status: foundation only / implementation not started. Independent educational project by Abdelrahman Ahmed. This repository is not a reconstruction of employer systems, a production deployment or proof of completed work.

## The engineering challenge

Create a practical teaching kit using the independent labs: a Python debugging workshop, an AWS event-processing lab and a Git collaboration simulation. Design learner outcomes and assessment before recording content.

This is a capstone for an experienced engineer. The goal is to defend tradeoffs, investigate failure and produce reproducible evidence, not just get a happy-path demo running.

**Technical focus:** Technical education · Python · AWS · Git · Mentoring · Curriculum design.

## What exists in this first commit

- A project-specific architecture brief and decision questions.
- Five implementation milestones with explicit review gates.
- Failure experiments and acceptance criteria.
- Typed Python interface scaffolds. Methods deliberately raise `NotImplementedError`.
- One synthetic scenario fixture; it is an input, not a successful output or benchmark.
- Evidence and journal templates, an issue template, and syntax/JSON foundation checks.

## What you will build

1. Define learner personas, prerequisites and observable outcomes. Build a diagnostic exercise that separates syntax gaps from systems reasoning.
2. Create a Python debugging workshop with a broken example, instructor solution boundaries and a rubric; cover API validation and authorization failure cases.
3. Create an AWS event lab using synthetic data and an offline path. Teach retries, idempotency and resource cleanup; identify what requires a real cloud account.
4. Create a Git simulation with feature branches, a conflict, a revert and a review checklist. Keep all history and collaborators fictional.
5. Pilot with a self-review or consenting learner; label the evidence accurately. Add accessible handouts, transcripts, formative checks and a revision log.

## Start here

1. Read [the architecture brief](docs/architecture.md) and record the first decision in [ADR 0001](docs/adr/0001-system-boundaries.md).
2. Inspect [the synthetic scenario](examples/scenario.json) and [the interface boundary](src/technical_teaching_studio/interfaces.py).
3. Run the foundation checks from the repository root:

   ```sh
   python3 tools/check_foundation.py
   ```

   Python 3.9+ is sufficient for these standard-library checks. They parse Python and JSON; they do **not** validate runtime behavior, deployment safety, protocol compliance or completion.
4. Create a feature branch, implement milestone 1 and add behavior tests before adapters.
5. Follow [the milestone backlog](docs/milestones.md). Select and pin implementation dependencies when you introduce them; none are installed by this scaffold.
6. Complete [the failure lab](docs/failure-lab.md), gather [evidence](docs/evidence/README.md) and review [acceptance criteria](docs/acceptance.md).

There is deliberately no `deploy`, `apply`, paid API call, installed cloud SDK or working runtime in this initial commit.

## Architecture at a glance

```text
Learning outcomes -> diagnostics -> guided labs -> independent challenge
                                                      |
                                          rubric / feedback / revision
```

This is a proposed lab architecture. [The design brief](docs/architecture.md) identifies decisions still to make.

## Learning prerequisites

- `application-engineering-lab` (a suggested learning prerequisite; no runtime dependency is wired in)
- `aws-live-events-lab` (a suggested learning prerequisite; no runtime dependency is wired in)

Repositories are separate and can evolve independently. If you connect them later, exchange versioned fixtures or contracts; do not rely on sibling-relative imports. You can implement a standalone synthetic adapter first.

## What makes this substantial

- Guided lab versus independent assessment
- Local alternatives versus cloud fidelity
- Evidence-based grading and accessible materials

You must explain what happens on retries, partial failure, concurrent operations and recovery. Record what your test environment cannot prove. No result is accepted simply because a dashboard is green.

## Definition of done

- Each learning outcome maps to an exercise and an observable rubric criterion.
- Instructor guidance explains common misconceptions and gives graduated hints.
- Cloud cleanup and local alternatives are explicit.
- Feedback or outcome claims distinguish self-review from actual learner evidence.

Also supply installation/reproduction instructions, dependency versions, meaningful behavior tests, cleanup instructions, an architecture decision log and evidence from a repeatable demonstration. A checklist or syntax check alone does not satisfy completion.

## Advanced extensions

- Arabic and English lesson variants
- MATLAB/Python comparison lesson using synthetic engineering signals
- Cybersecurity module on API object-level authorization
- Package a workshop outline suitable for future Edurima delivery

Extensions follow a working baseline; they are not requirements for the first milestone.

## Boundaries and costs

Use fictional services, synthetic inputs and a disposable sandbox. Do not copy employer repositories, runbooks, tickets, customer data, credentials or internal architecture. Real cloud/provider adapters are future work and may incur costs; [the operations plan](docs/operations.md) must identify account, region, budget, resource inventory and teardown before deployment. Budget alerts notify; they do not constitute a hard spending cap.

## Publishable evidence, when earned

A completed lab may support a portfolio case study labeled **independent project**. Share your original code, sanitized diagrams, measured results and a failure/recovery write-up. Employer experience and personal lab evidence remain separate. Never copy illustrative fixture values into a results claim.

## Primary references

- https://docs.python.org/3/tutorial/
- https://git-scm.com/book/en/v2
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html

Read current official documentation when selecting SDKs, images, tool versions and integrations. The scaffold intentionally does not guess compatible version combinations.

## Repository map

- `src/technical_teaching_studio/interfaces.py`
- `examples/scenario.json`
- `docs/architecture.md`
- `docs/milestones.md`
- `docs/failure-lab.md`
- `docs/acceptance.md`
- `docs/learning-journal.md`
- `docs/evidence/README.md`
- `docs/operations.md` — local/cloud boundaries and teardown plan.
- `docs/adr/` — decisions and alternatives.
- `tools/check_foundation.py` — syntax and fixture integrity only.

## Working agreement

Keep commits focused: `docs`, `feat`, `test`, `fix`, `ops`. Work on a feature branch and merge only after the milestone review. Consult [CONTRIBUTING.md](CONTRIBUTING.md). No open-source license has been chosen yet; see [NOTICE.md](NOTICE.md).

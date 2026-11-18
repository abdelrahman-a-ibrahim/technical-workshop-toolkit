# Technical Workshop Toolkit

Versioned technical workshop materials, assessment contracts and instructor delivery resources.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

A toolkit for authoring and delivering practical workshops in Python, cloud engineering and Git collaboration. It organizes prerequisites, runnable examples, assessment rubrics, instructor guidance and accessible participant materials into a versioned delivery package.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Versioned Python, cloud and Git workshop delivery packages.
- Participant prerequisites, diagnostics and accessible exercise materials.
- Observable assessment criteria and structured feedback contracts.
- Instructor guidance, progressive hints and local alternatives for cloud dependencies.
- Reviewable lesson revisions and delivery outcome records.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Learning outcomes -> diagnostics -> practical exercises -> independent challenge
                                                      |
                                          rubric / feedback / revision
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

Technical education · Python · AWS · Git · Mentoring · Workshop design.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/technical-workshop-toolkit.git
cd technical-workshop-toolkit
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/technical_workshop_toolkit/interfaces.py`](src/technical_workshop_toolkit/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- Each learning outcome maps to an exercise and an observable rubric criterion.
- Instructor guidance explains common misconceptions and gives graduated hints.
- Cloud cleanup and local alternatives are explicit.
- Feedback or outcome claims distinguish self-review from actual learner evidence.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/technical_workshop_toolkit/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://docs.python.org/3/tutorial/
- https://git-scm.com/book/en/v2
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html

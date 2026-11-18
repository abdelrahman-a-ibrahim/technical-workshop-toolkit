# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
A toolkit for authoring and delivering practical workshops in Python, cloud engineering and Git collaboration. It organizes prerequisites, runnable examples, assessment rubrics, instructor guidance and accessible participant materials into a versioned delivery package.

## Questions
- Guided development environment versus independent assessment
- Local alternatives versus cloud fidelity
- Evidence-based grading and accessible materials

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.

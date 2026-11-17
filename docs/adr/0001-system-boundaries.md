# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Create a practical teaching kit using the independent labs: a Python debugging workshop, an AWS event-processing lab and a Git collaboration simulation. Design learner outcomes and assessment before recording content.

## Decision questions
- Guided lab versus independent assessment
- Local alternatives versus cloud fidelity
- Evidence-based grading and accessible materials

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.

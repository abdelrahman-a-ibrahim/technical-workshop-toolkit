# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
A toolkit for authoring and delivering practical workshops in Python, cloud engineering and Git collaboration. It organizes prerequisites, runnable examples, assessment rubrics, instructor guidance and accessible participant materials into a versioned delivery package.

## Component view
```text
Learning outcomes -> diagnostics -> practical exercises -> independent challenge
                                                      |
                                          rubric / feedback / revision
```

## Design decisions
- Guided development environment versus independent assessment
- Local alternatives versus cloud fidelity
- Evidence-based grading and accessible materials

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/technical_workshop_toolkit/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.

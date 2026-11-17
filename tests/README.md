# Behavior test plan

No implementation tests exist yet. Foundation checks do not count as behavior tests.

Build meaningful tests as each behavior is implemented:
1. Domain tests for invariants and explicit error results.
2. Adapter contract tests, including malformed and unauthorized inputs.
3. Integration tests against actual chosen dependencies, isolated from production.
4. Relevant concurrency, retry, crash/restart and recovery tests.
5. One reproducible end-to-end acceptance scenario.

Use `docs/failure-lab.md` and `docs/acceptance.md` for project-specific cases. A mock cannot establish real service ordering, consistency, replication or durability guarantees. Label simulator coverage and real-dependency coverage separately.

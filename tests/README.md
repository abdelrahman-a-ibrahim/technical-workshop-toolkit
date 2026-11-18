# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- Each learning outcome maps to an exercise and an observable rubric criterion.
- Instructor guidance explains common misconceptions and gives graduated hints.
- Cloud cleanup and local alternatives are explicit.
- Feedback or outcome claims distinguish self-review from actual learner evidence.

## Failure coverage
- Explain why a duplicate event is not necessarily a bug in the queue.
- Guide a learner who confuses authentication with authorization.
- Recover a deliberately broken Git branch without losing intended changes.
- Adapt a cloud exercise for a learner without an AWS account.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.

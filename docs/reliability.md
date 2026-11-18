# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Explain why a duplicate event is not necessarily a bug in the queue.
- Guide a learner who confuses authentication with authorization.
- Recover a deliberately broken Git branch without losing intended changes.
- Adapt a cloud exercise for a learner without an AWS account.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- Each learning outcome maps to an exercise and an observable rubric criterion.
- Instructor guidance explains common misconceptions and gives graduated hints.
- Cloud cleanup and local alternatives are explicit.
- Feedback or outcome claims distinguish self-review from actual learner evidence.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.

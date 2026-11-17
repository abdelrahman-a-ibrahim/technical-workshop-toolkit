# Development workflow

This repository begins as a foundation. Implement one milestone at a time.

1. Read the relevant milestone and propose an ADR where the choice affects guarantees.
2. Create a feature branch from `main`.
3. Add behavior tests for one invariant, then implement the smallest useful change.
4. Select and pin dependencies intentionally; record why they are required.
5. Run foundation checks and the new implementation’s tests.
6. Run the relevant failure exercise in a disposable environment.
7. Update status, evidence and setup/cleanup instructions before merging.

Commit examples: `docs: decide checkpoint boundary`, `feat: add idempotent state update`, `test: cover restart after acknowledgement failure`.

Do not merge copied internal code, secrets or unverified benchmark claims. The foundation check is not a deployment or milestone approval gate.

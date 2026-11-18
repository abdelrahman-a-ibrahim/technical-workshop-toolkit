# Development workflow

1. Define the intended behavior and acceptance criteria from `docs/requirements.md`.
2. Create a feature branch from `main`.
3. Implement one coherent behavior with meaningful tests.
4. Pin dependencies when introduced and record architecture decisions.
5. Run `python3 tools/check_project.py` plus relevant implementation tests.
6. Exercise relevant failure/recovery scenarios in an isolated environment.
7. Update setup, delivery status, operational documentation and measured results before merging.

Review staged changes before committing. Keep credentials, generated cloud state and non-public third-party material outside the repository. A successful source check is not a runtime or release readiness gate.

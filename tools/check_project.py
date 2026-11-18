"""Source integrity checks only; runtime behavior is not implemented or tested here."""
import ast
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ["README.md", "docs/architecture.md", "docs/requirements.md",
            "docs/roadmap.md", "docs/reliability.md", "docs/operations.md",
            "examples/scenario.json"]
for name in required:
    if not (root / name).is_file():
        raise SystemExit("Missing project file: " + name)
count = 0
for folder in ("src", "tools", "examples"):
    for path in (root / folder).rglob("*"):
        if path.suffix == ".py":
            ast.parse(path.read_text(), filename=str(path))
            count += 1
        elif path.suffix == ".json":
            json.loads(path.read_text())
            count += 1
print("Source integrity OK: %d Python/JSON files parsed. Runtime behavior is untested." % count)

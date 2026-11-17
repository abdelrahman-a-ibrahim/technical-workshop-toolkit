"""Proposed application boundary for Technical Teaching Studio.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class AssessmentRubric:
    def assess(self, submission: dict, criteria: list) -> dict:
        """Evaluate observable evidence rather than completion alone."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def feedback(self, assessment: dict) -> list:
        """Produce actionable next steps tied to each unmet criterion."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")


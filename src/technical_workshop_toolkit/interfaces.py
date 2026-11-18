"""Initial application boundary for Technical Workshop Toolkit.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class AssessmentRubric:
    def assess(self, submission: dict, criteria: list) -> dict:
        """Evaluate observable evidence rather than completion alone."""
        raise NotImplementedError("Runtime implementation is in development.")

    def feedback(self, assessment: dict) -> list:
        """Produce actionable next steps tied to each unmet criterion."""
        raise NotImplementedError("Runtime implementation is in development.")

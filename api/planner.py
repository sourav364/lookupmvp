"""LLM plan compiler stub."""
from typing import Any, Dict


def compile_plan(question: str) -> Dict[str, Any]:
    """Return a fixed plan for a given question.

    In future iterations this will call an LLM to produce a plan for
    analytics execution.
    """

    return {"query": "(stub)"}

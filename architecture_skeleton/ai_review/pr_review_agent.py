"""ai_review/pr_review_agent.py - redact, score risk, run the LangGraph agent (or
a local fallback), validate any fix, post the result. [Omitted - see README.]"""
from typing import TypedDict


class RiskResult(TypedDict):
    """low/medium/high + reasons. A detected secret alone forces the top band."""
    risk_level: str
    risk_reasons: list[str]


def compute_risk_heuristic(raw_diff: str, guardrail_flags: list[str]) -> RiskResult:
    """Deterministic, point-based risk scoring - not another LLM call."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


class AgentState(TypedDict):
    """The real LangGraph state threaded through the reasoning loop."""
    redacted_diff: str
    risk_level: str
    messages: list


def build_review_graph() -> object:
    """LangGraph StateGraph: reason -> tool -> reason, until confident."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


def local_fallback_review(raw_diff: str, guardrail_flags: list[str]) -> dict:
    """Deterministic reviewer used whenever the AI path is unavailable."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


class AnchorableFix(TypedDict):
    """A proposed fix, trusted only once independently verified against the diff."""
    file: str
    line: int
    suggestion: str


def validate_anchorable_fix(raw_diff: str, claimed_file: str, claimed_line: int) -> bool:
    """Re-derives real added lines from the diff's hunk headers; checks the claim."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


def post_review(result: dict) -> bool:
    """Posts the review comment, plus any validated fix as a one-click suggestion."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


def review_diff(raw_diff: str) -> dict:
    """Entry point: redact -> score -> review -> validate -> return the report."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")

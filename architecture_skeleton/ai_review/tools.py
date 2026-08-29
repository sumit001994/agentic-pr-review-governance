"""ai_review/tools.py - the four read-only tools the agent can call. Every return
value is redacted before it can re-enter the reasoning loop. [Omitted - see README.]"""
from typing import Any, Callable


def _redact_result(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Skeleton no-op (real wrapper omitted, stays safely importable)."""
    return fn


@_redact_result
def get_file_context(file_path: str, around_line: int | None = None) -> str:
    """Reads more of a file when the diff cuts off mid-method."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


@_redact_result
def check_dependency_vulnerabilities(package_name: str, version: str) -> dict:
    """Checks a real CVE database against a changed library version."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


@_redact_result
def run_targeted_test(test_name: str) -> dict:
    """Runs one test; reports 'nothing verified' instead of a false pass."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


@_redact_result
def get_related_code_context(symbol_name: str) -> str:
    """Finds other files referencing the changed class or symbol."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")


TOOLS: list[Callable[..., Any]]

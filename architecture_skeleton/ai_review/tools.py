"""ai_review/tools.py - the four real, read-only tools the review agent can choose
to call. Every tool's return value passes through a redaction decorator at its own
return boundary before it can ever re-enter the agent's reasoning loop - a second,
independent redaction layer on top of the diff-level one, closing a real gap where
a tool's own raw output (e.g. a file read straight off disk) could otherwise reach
the model unredacted. None of these tools can write to the repository.

[Real implementations omitted from this public skeleton - see README.]
"""
from typing import Any, Callable


def _redact_result(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Wraps a tool function so its return value is redacted before the agent ever
    sees it - applied uniformly to all four tools below, not selectively.

    Skeleton note: unlike the tool functions below, this decorator is applied at
    import time (`@_redact_result` runs when the module loads, not when a tool is
    later called) - so it's left as a real no-op here rather than raising, to keep
    this file safely importable. The real implementation's actual wrapping logic is
    omitted; see README."""
    return fn


@_redact_result
def get_file_context(file_path: str, around_line: int | None = None) -> str:
    """Reads more of a real file when the diff cuts off mid-method."""
    raise NotImplementedError("Implementation omitted from this public skeleton - see README.")


@_redact_result
def check_dependency_vulnerabilities(package_name: str, version: str) -> dict:
    """Checks a real vulnerability database against a specific library version."""
    raise NotImplementedError("Implementation omitted from this public skeleton - see README.")


@_redact_result
def run_targeted_test(test_name: str) -> dict:
    """Actually runs one relevant test and reports the real result - including an
    explicit 'nothing was actually verified' outcome when no test matches, rather
    than a false pass (a real bug found and fixed in this exact tool - see README)."""
    raise NotImplementedError("Implementation omitted from this public skeleton - see README.")


@_redact_result
def get_related_code_context(symbol_name: str) -> str:
    """Finds other real files that reference the changed class or symbol."""
    raise NotImplementedError("Implementation omitted from this public skeleton - see README.")


TOOLS: list[Callable[..., Any]]

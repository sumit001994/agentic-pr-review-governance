"""ai_review/guardrails.py - redacts secrets from a diff before any LLM sees it.
Regex-based, not AI-based, by design. [Patterns omitted - see README.]"""
import re
from typing import Callable

REDACTED_MARKER: str
_PATTERNS: "list[tuple[str, re.Pattern[str], str | Callable[[re.Match[str]], str]]]"


def redact(text: str) -> tuple[str, list[str]]:
    """Returns (redacted_text, flags). Implementation omitted - see README."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")

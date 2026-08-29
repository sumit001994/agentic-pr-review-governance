"""ai_review/guardrails.py - redacts likely-sensitive content out of a diff BEFORE
it is sent to any LLM. Deliberately regex/pattern-based, not AI-based: a guardrail
that itself depends on an LLM call to decide what's sensitive is circular. Matches
six real, well-known credential/secret shapes.

[Real patterns and matching logic omitted from this public skeleton - see README.]
"""
import re
from typing import Callable


REDACTED_MARKER: str

# Six real patterns fire here in the real implementation: a generic key/secret/
# token/password assignment (with a capturing-group fix so redaction can never
# leave invalid code behind - see README), an AWS access key, a PEM private key
# block, a credentialed connection string, an email address, and a Bearer token.
_PATTERNS: list[tuple[str, "re.Pattern[str]", "str | Callable[[re.Match[str]], str]"]]


def redact(text: str) -> tuple[str, list[str]]:
    """Returns (redacted_text, flags) - flags names each pattern that fired, so the
    caller can report how many potentially sensitive items were removed, without
    ever having to re-expose what they were."""
    raise NotImplementedError("Implementation omitted from this public skeleton - see README.")

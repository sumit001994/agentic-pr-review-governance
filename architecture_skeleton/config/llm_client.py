"""config/llm_client.py - resolves the LLM client the agent uses. Tries real
Workload Identity Federation via Vertex AI first (a short-lived, auto-issued
credential, proactively refreshed before a long multi-tool reasoning turn could
ever get caught mid-call), falling back to a static API key only where there is
genuinely no CI identity to federate with - a local developer machine.

[Real refresh-timing logic omitted from this public skeleton - see README.]
"""
import datetime
from typing import Any, Callable


class GeminiCredentialProvider:
    """Isolates credential rotation from the agent's reasoning loop entirely - the
    agent never imports or calls this class, it only ever receives a finished,
    ready-to-use model object. Proactively refreshes before expiry rather than
    reacting to a failed call."""

    def __init__(self, credentials: Any, clock: "Callable[[], datetime.datetime] | None" = None) -> None:
        raise NotImplementedError("Implementation omitted from this public skeleton - see README.")

    def get_valid_token(self) -> str:
        """The one method anything outside this class is allowed to call."""
        raise NotImplementedError("Implementation omitted from this public skeleton - see README.")

    def _needs_refresh(self) -> bool:
        raise NotImplementedError("Implementation omitted from this public skeleton - see README.")

    def _refresh(self) -> None:
        raise NotImplementedError("Implementation omitted from this public skeleton - see README.")


def get_llm() -> "object":
    """Tries a real Vertex AI + Workload Identity Federation path first (gated on
    a real cloud project being configured), falls back to a static API key path
    otherwise - kept deliberately, not deleted, as the honest local-dev answer."""
    raise NotImplementedError("Implementation omitted from this public skeleton - see README.")

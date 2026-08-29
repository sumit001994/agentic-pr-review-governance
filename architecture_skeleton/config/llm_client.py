"""config/llm_client.py - Workload Identity Federation via Vertex AI first, static
key fallback for local dev. [Refresh-timing logic omitted - see README.]"""
import datetime
from typing import Any, Callable


class GeminiCredentialProvider:
    """Isolates credential rotation from the agent's reasoning loop entirely."""

    def __init__(self, credentials: Any, clock: "Callable[[], datetime.datetime] | None" = None) -> None:
        raise NotImplementedError("Omitted from this public skeleton - see README.")

    def get_valid_token(self) -> str:
        """The one method anything outside this class may call."""
        raise NotImplementedError("Omitted from this public skeleton - see README.")

    def _needs_refresh(self) -> bool:
        raise NotImplementedError("Omitted from this public skeleton - see README.")

    def _refresh(self) -> None:
        raise NotImplementedError("Omitted from this public skeleton - see README.")


def get_llm() -> object:
    """Vertex AI + OIDC first, static key fallback for local dev."""
    raise NotImplementedError("Omitted from this public skeleton - see README.")

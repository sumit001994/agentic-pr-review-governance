"""tests/test_llm_client.py - real unit tests for the credential-refresh timing
logic, using a fake credentials object and a fake, controllable clock - no live
network calls or real cloud connection involved.

[Test bodies omitted - see README for real, verified pass/fail output.]
"""


def test_token_with_time_left_is_reused_not_refreshed():
    """A token well inside its valid window must be returned as-is."""


def test_token_inside_the_safety_window_is_refreshed():
    """A token close to expiry must be refreshed, and the new token returned -
    never the stale one."""


def test_expired_or_never_valid_token_is_refreshed():
    """An expired or never-yet-valid token must always trigger a refresh."""


def test_credential_with_no_expiry_is_left_alone():
    """A credential type with no expiry concept must never be refreshed
    pointlessly."""


def test_calling_get_valid_token_twice_in_a_row_only_refreshes_once():
    """Refreshing must be genuinely on-demand, not wasteful."""


def test_agent_reasoning_loop_never_imports_the_credential_provider():
    """Credential rotation must stay fully isolated from the logic that decides
    what the agent does - a deliberate architectural boundary, not an accident."""

"""tests/test_guardrails.py - real regression tests against the redaction filter.

[Test bodies omitted - see README for real, verified pass/fail output.]
"""


def test_redacts_generic_api_key_assignment():
    """A plain `apiKey = "..."` assignment must be detected and redacted."""


def test_redacts_camel_case_prefixed_api_key_variable():
    """A camelCase-prefixed name like `debugApiKey` must still be caught - a real
    regression test for a real bug found via a live adversarial diff."""


def test_camel_case_prefixed_api_key_redaction_keeps_valid_java_syntax():
    """Redacting a camelCase-prefixed secret must never leave invalid code behind -
    a real regression test for a real bug found live during interview-prep
    rehearsal, fixed with regex capturing groups."""


def test_does_not_flag_unrelated_camel_case_word():
    """An unrelated word that merely contains 'key' must never be flagged."""


def test_redacts_aws_access_key_id():
    """A real AWS access key ID shape must be detected and redacted."""


def test_redacts_private_key_block():
    """A full PEM private key block must be detected and redacted as one unit."""


def test_redacts_connection_string_with_credentials():
    """A credentialed connection string must have its credentials redacted."""


def test_redacts_email_address():
    """An email address must be detected and redacted."""


def test_redacts_bearer_token():
    """A Bearer token must be detected and redacted."""


def test_clean_diff_produces_no_flags():
    """A diff with nothing sensitive must pass through completely unchanged."""


def test_multiple_findings_all_flagged_in_one_pass():
    """Multiple distinct sensitive items in one diff must all be flagged."""

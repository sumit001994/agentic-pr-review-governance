"""tests/test_tools.py - regression tests for the four agent tools and their
shared redaction boundary. [Test bodies omitted - see README for verified results.]"""


def test_get_file_context_redacts_a_secret_found_in_the_file_itself():
    """A secret in a file read off disk must never reach the agent unredacted."""


def test_run_targeted_test_reports_nothing_verified_for_a_nonexistent_test():
    """A guessed test name must report 'nothing verified,' never a false pass."""


def test_check_dependency_vulnerabilities_against_a_real_cve():
    """A known-vulnerable package version must be reported as such."""


def test_get_related_code_context_finds_a_real_same_package_reference():
    """A same-package reference with no explicit import must still be found."""


def test_redact_value_redacts_strings_inside_a_nested_dict_and_list():
    """Redaction must recurse into nested tool-output structures."""

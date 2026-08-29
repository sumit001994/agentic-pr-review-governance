"""
Illustrative excerpt — NOT the full working module.

Demonstrates one specific design decision from the real project: an AI's claimed
"fix this file at this line" suggestion is never trusted just because the model
said so. An AI counting diff lines is exactly the kind of arithmetic it can get
subtly wrong - so a separate, deterministic function independently re-derives the
real added line numbers straight from the diff's own unified-diff hunk headers
(`@@ -a,b +c,d @@`), and only agrees the claimed line is real if it appears in that
independently-computed set.

This file is standalone and simplified for illustration - it omits real-world
hunk-header edge cases (multiple hunks per file, no-newline-at-end-of-file markers)
covered in the real implementation, and is not runnable as part of the real system.
"""
import re

_HUNK_HEADER_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")


def real_added_lines(diff_text: str) -> set[int]:
    """Returns the set of line numbers that are genuinely new/added in the diff's
    resulting file - derived independently from the diff text itself, never from
    an AI's own claim about what it added."""
    added: set[int] = set()
    new_line_num = 0
    in_hunk = False

    for raw_line in diff_text.splitlines():
        header_match = _HUNK_HEADER_RE.match(raw_line)
        if header_match:
            new_line_num = int(header_match.group(1))
            in_hunk = True
            continue
        if not in_hunk:
            continue
        if raw_line.startswith("+") and not raw_line.startswith("+++"):
            added.add(new_line_num)
            new_line_num += 1
        elif raw_line.startswith("-") and not raw_line.startswith("---"):
            continue  # removed line - doesn't exist in the new file, don't advance
        else:
            new_line_num += 1  # unchanged context line

    return added


def fix_claim_is_verifiable(diff_text: str, claimed_line: int) -> bool:
    """The actual trust boundary: an AI-claimed line is only treated as real once
    it's confirmed to genuinely be part of what was added, not assumed correct
    because the model sounded confident."""
    return claimed_line in real_added_lines(diff_text)

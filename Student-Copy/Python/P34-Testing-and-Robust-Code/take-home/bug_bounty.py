# TAKE-HOME PROJECT: Bug Bounty
# After lesson P34 (Testing and Robust Code) - about 1–2 hours, in chunks over the next few days.
#
# The starter is a little "text utilities" module with 5 hidden bugs. Your job: write
# tests that FIND them, then fix the code. Real testers do exactly this.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Read each function's docstring – that's the spec of what it SHOULD do
#   [ ] 2. Write at least 2 pytest tests per function in test_bug_bounty.py (normal +
#          boundary + erroneous data)
#   [ ] 3. Run pytest -v (venv active!) – every failing test is a bug found
#   [ ] 4. Fix the bugs one at a time until everything passes
#   [ ] 5. Write a short bug report in a comment: what was wrong in each function
#
# Stretch: Add a new function is_valid_email(s) – write the tests FIRST (TDD), then the
# code.
#
# Bring it to the next session - working or stuck, both are fine.

def word_count(text):
    """Return the number of words in text (words are separated by spaces)."""
    return len(text.split(" "))


def capitalise_words(text):
    """Return text with the first letter of every word in capitals."""
    return " ".join(w[0].upper() + w[1:] for w in text.split(" "))


def is_palindrome(text):
    """True if text reads the same backwards, ignoring case and spaces."""
    clean = text.replace(" ", "")
    return clean == clean[::-1]


def average_word_length(text):
    """Average length of the words, or 0 for empty text."""
    words = text.split()
    return sum(len(w) for w in words) / len(words)


def truncate(text, n):
    """Cut text to at most n characters, adding '...' if it was cut (the '...' counts towards n)."""
    if len(text) <= n:
        return text
    return text[:n] + "..."

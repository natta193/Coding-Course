def word_count(text):
    """Return the number of words in text (words are separated by spaces)."""
    return len(text.split())          # BUG 1: split(" ") counted empty strings for double spaces / ""


def capitalise_words(text):
    """Return text with the first letter of every word in capitals."""
    return " ".join(w[0].upper() + w[1:] for w in text.split())   # BUG 2: crashed on double spaces (w = "")


def is_palindrome(text):
    """True if text reads the same backwards, ignoring case and spaces."""
    clean = text.replace(" ", "").lower()   # BUG 3: forgot to ignore case
    return clean == clean[::-1]


def average_word_length(text):
    """Average length of the words, or 0 for empty text."""
    words = text.split()
    if not words:                      # BUG 4: ZeroDivisionError on ""
        return 0
    return sum(len(w) for w in words) / len(words)


def truncate(text, n):
    """Cut text to at most n characters, adding '...' if it was cut (the '...' counts towards n)."""
    if len(text) <= n:
        return text
    return text[: n - 3] + "..."       # BUG 5: result was n + 3 long


# ---- test_bug_bounty.py (tests shown here so this file runs on its own) ----
def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("hello  world") == 2
    assert word_count("") == 0

def test_capitalise():
    assert capitalise_words("hello world") == "Hello World"
    assert capitalise_words("a  b") == "A B"

def test_palindrome():
    assert is_palindrome("Never odd or even")
    assert not is_palindrome("python")

def test_average():
    assert average_word_length("ab abcd") == 3
    assert average_word_length("") == 0

def test_truncate():
    assert truncate("hello", 10) == "hello"
    assert truncate("hello world", 8) == "hello..."
    assert len(truncate("abcdefghijk", 6)) == 6


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All tests pass")

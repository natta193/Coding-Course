# file: maths.py
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# file: test_maths.py
from maths import is_leap

def test_normal_leap():
    assert is_leap(2024)

def test_normal_non_leap():
    assert not is_leap(2023)

def test_century_boundaries():
    assert not is_leap(1900)
    assert is_leap(2000)

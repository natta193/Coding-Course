def is_valid_password(pw):
    return (8 <= len(pw) <= 20
            and any(c.isdigit() for c in pw)
            and any(c.isupper() for c in pw)
            and any(c.islower() for c in pw)
            and " " not in pw)

def test_valid():
    assert is_valid_password("Secret123")

def test_too_short_boundary():
    assert not is_valid_password("Sec1234")      # 7 chars
    assert is_valid_password("Secr1234")         # 8 chars

def test_too_long_boundary():
    assert is_valid_password("A1" + "a" * 18)    # 20 chars
    assert not is_valid_password("A1" + "a" * 19)

def test_needs_digit():
    assert not is_valid_password("SecretPass")

def test_needs_upper():
    assert not is_valid_password("secret123")

def test_needs_lower():
    assert not is_valid_password("SECRET123")

def test_no_spaces():
    assert not is_valid_password("Secret 123")

def test_empty():
    assert not is_valid_password("")

if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All tests passed")

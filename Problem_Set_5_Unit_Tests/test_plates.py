from plates import is_valid

def main():
    test_is_valid_7char()
    test_is_valid_6char()
    test_is_valid_5char()
    test_is_valid_4char()
    test_is_valid_3char()
    test_is_valid_2char()
    test_is_valid_alpaftnum()


def test_is_valid_7char():
    assert is_valid("GOODBYE") == False

def test_is_valid_6char():
    assert is_valid("HELLOO") == True

def test_is_valid_5char():
    assert is_valid("HELLO") == True

def test_is_valid_4char():
    assert is_valid("CS50") == True

def test_is_valid_alpaftnum():
    assert is_valid("CS05") == False

def test_is_valid_3char():
    assert is_valid("AAA") == True

def test_is_valid_2char():
    assert is_valid("AA") == True


if __name__ == "__main__":
    main()
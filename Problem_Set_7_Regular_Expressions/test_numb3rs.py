from numb3rs import validate


def main():
    test_validate_true()
    test_validate_false()

def test_validate_true():
    assert validate("127.0.0.1") == True

def test_validate_false():
    assert validate("275.3.6.28") == False

if __name__ == "__main__":
    main()
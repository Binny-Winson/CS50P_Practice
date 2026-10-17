from bank import value

def main():
    test_value_hello()
    test_value_h()
    test_value_random()
    test_value_digit()

def test_value_hello():
    assert value("HELLO") == 0

def test_value_h():
    assert value("HEY") == 20

def test_value_random():
    assert value("Good Morning") == 100

def test_value_digit():
    assert value("500") == 100

if __name__ == "__main__":
    main()
import pytest
from jar import Jar


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    


def test_init():
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0

    jar.deposit(11)
    assert jar.size == 11

    custom_jar = Jar(20)
    assert custom_jar.capacity == 20

    with pytest.raises(ValueError):
        Jar(-5)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.deposit(12)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.withdraw(6)


if __name__ == "__main__":
    main()
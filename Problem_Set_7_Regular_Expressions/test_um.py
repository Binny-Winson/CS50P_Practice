from um import count


def main():
    test_count_1()
    test_count_2()
    test_count_3()

def test_count_1():
    assert count("um") == 1

def test_count_2():
    assert count("Um, thanks, um...") == 2

def test_count_3():
    assert count("um, hello, um, world, um") == 3

if __name__ == "__main__":
    main()
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("2/4") == 50

def test_gauge():
    assert gauge(100) == "F"

if __name__ == "__main__":
    main()
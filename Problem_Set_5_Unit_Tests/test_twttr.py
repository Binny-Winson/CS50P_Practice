from twttr import shorten

def main():
    test_shorten_alpha_caps()
    test_shorten_alpha_small()
    test_shorten_digit()

def test_shorten_alpha_caps():
    assert shorten("HELLO") == "Output: HLL"

def test_shorten_alpha_small():
    assert shorten("hello") == "Output: hll"

def test_shorten_digit():
    assert shorten("500") == "Output: 500"

if __name__ == "__main__":
    main()


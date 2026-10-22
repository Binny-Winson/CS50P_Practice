import pytest
from working import convert


def main():
    test_AMtoPM()
    test_PMtoAM()
    test_wrong_sep()
    test_wrong_time_format()

def test_AMtoPM():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_PMtoAM():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_wrong_time_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_wrong_sep():
    with pytest.raises(ValueError):
        convert("9 PM - 5 AM")

if __name__ == "__main__":
    main()
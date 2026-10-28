from datetime import datetime

import pytest
from seasons import get_date, min_to_words


def main():
    test_get_date()
    test_invalid_date()
    test_min_to_words()

def test_get_date():
    assert get_date("2025-10-29") == datetime(2025, 10, 29, 0, 0)

def test_invalid_date():
    with pytest.raises(SystemExit) as exc_info:
        get_date("2025-Oct-29")
    assert str(exc_info.value) == "Invalid date"

def test_min_to_words():
    target_date = get_date("2025-10-29")
    assert min_to_words(target_date) == "Five hundred twenty-five thousand, six hundred minutes"

if __name__ == "__main__":
    main()
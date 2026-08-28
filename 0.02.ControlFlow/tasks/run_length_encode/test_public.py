from run_length_encode import run_length_encode


def test_simple() -> None:
    assert run_length_encode("aaabbc") == "a3b2c1"


def test_no_repeats() -> None:
    assert run_length_encode("abc") == "a1b1c1"


def test_empty() -> None:
    assert run_length_encode("") == ""

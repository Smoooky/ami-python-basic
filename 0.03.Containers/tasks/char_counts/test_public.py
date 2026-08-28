from char_counts import char_counts


def test_simple() -> None:
    assert char_counts("abba") == {"a": 2, "b": 2}


def test_case_matters() -> None:
    assert char_counts("aAa") == {"a": 2, "A": 1}


def test_empty() -> None:
    assert char_counts("") == {}

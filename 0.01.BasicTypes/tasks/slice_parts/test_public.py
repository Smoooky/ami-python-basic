from slice_parts import slice_parts


def test_six_chars() -> None:
    assert slice_parts("abcdef") == ("fedcba", "ace", "def")


def test_short_string() -> None:
    assert slice_parts("ab") == ("ba", "a", "ab")


def test_empty() -> None:
    assert slice_parts("") == ("", "", "")

from encoding_stats import encoding_stats


def test_ascii() -> None:
    assert encoding_stats("abc") == (3, 3, 6, True)


def test_accented() -> None:
    assert encoding_stats("café") == (4, 5, 8, False)


def test_empty_is_ascii() -> None:
    assert encoding_stats("") == (0, 0, 0, True)

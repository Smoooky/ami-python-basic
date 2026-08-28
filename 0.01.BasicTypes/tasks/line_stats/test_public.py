from line_stats import line_stats


def test_three_numbers() -> None:
    assert line_stats("1 2 3") == (3, 6, 3, 1, 2.0)


def test_single_number() -> None:
    assert line_stats("42") == (1, 42, 42, 42, 42.0)


def test_extra_spaces() -> None:
    assert line_stats("  7   8  ") == (2, 15, 8, 7, 7.5)

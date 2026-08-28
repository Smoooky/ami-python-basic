from money_to_cents import money_to_cents


def test_thousands_separator() -> None:
    assert money_to_cents("1 234,56") == 123456


def test_value_that_breaks_naive_conversion() -> None:
    assert money_to_cents("1,15") == 115


def test_without_fraction() -> None:
    assert money_to_cents("1000") == 100000

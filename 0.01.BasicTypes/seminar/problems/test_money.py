from money import add_prices, close_enough, format_price, round_half_up, to_cents


def test_to_cents() -> None:
    assert to_cents("12.30") == 1230
    assert to_cents("0.05") == 5
    assert to_cents("0.00") == 0
    assert to_cents("100.99") == 10099


def test_to_cents_keeps_big_sums_exact() -> None:
    assert to_cents("99999999999999.99") == 9999999999999999


def test_format_price() -> None:
    assert format_price(1230) == "12.30"
    assert format_price(5) == "0.05"
    assert format_price(0) == "0.00"
    assert format_price(10099) == "100.99"


def test_format_price_is_the_inverse_of_to_cents() -> None:
    assert format_price(to_cents("0.00")) == "0.00"
    assert format_price(to_cents("0.07")) == "0.07"
    assert format_price(to_cents("12.30")) == "12.30"
    assert format_price(to_cents("100.99")) == "100.99"


def test_add_prices() -> None:
    assert add_prices("12.30", "0.70") == "13.00"
    assert add_prices("0.01", "0.02") == "0.03"
    assert add_prices("0.00", "0.00") == "0.00"
    assert add_prices("99.99", "0.01") == "100.00"


def test_add_prices_does_not_go_through_float() -> None:
    # 0.1 + 0.2 во float даёт 0.30000000000000004.
    assert add_prices("0.10", "0.20") == "0.30"


def test_round_half_up() -> None:
    assert round_half_up(2.5) == 3
    assert round_half_up(0.5) == 1
    assert round_half_up(1.4) == 1
    assert round_half_up(1.6) == 2
    assert round_half_up(7.0) == 7


def test_round_half_up_differs_from_round() -> None:
    assert round(0.5) == 0 and round_half_up(0.5) == 1
    assert round(2.5) == 2 and round_half_up(2.5) == 3


def test_round_half_up_on_negatives() -> None:
    assert round_half_up(-0.5) == 0
    assert round_half_up(-1.5) == -1
    assert round_half_up(-1.6) == -2


def test_close_enough() -> None:
    assert close_enough(0.1 + 0.2, 0.3) is True
    assert close_enough(1.0, 1.0) is True
    assert close_enough(1.0, 1.1) is False
    assert close_enough(2.0**53, 2.0**53 + 1) is True

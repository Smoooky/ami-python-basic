import pytest
from market_tick import Tick


def test_notional_and_repr() -> None:
    tick = Tick("AAPL", 150.25, 100)
    assert tick.notional() == 15025.0
    assert repr(tick) == "Tick('AAPL', 150.25, 100)"


def test_from_csv() -> None:
    assert Tick.from_csv("AAPL,150.25,100") == Tick("AAPL", 150.25, 100)


def test_typo_in_attribute_is_rejected() -> None:
    with pytest.raises(AttributeError):
        Tick("AAPL", 1.0, 1).prise = 1  # type: ignore[attr-defined]

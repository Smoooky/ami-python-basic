import pytest
from temperature import Temperature


def test_three_scales() -> None:
    t = Temperature(100)
    assert t.celsius == 100
    assert t.fahrenheit == 212.0
    assert t.kelvin == pytest.approx(373.15)


def test_write_through_fahrenheit() -> None:
    t = Temperature(100)
    t.fahrenheit = 32
    assert t.celsius == pytest.approx(0.0)
    assert t.kelvin == pytest.approx(273.15)


def test_validation_through_kelvin() -> None:
    t = Temperature(0)
    with pytest.raises(ValueError):
        t.kelvin = -1

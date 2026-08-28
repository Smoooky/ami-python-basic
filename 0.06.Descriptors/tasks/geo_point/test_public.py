import pytest
from geo_point import GeoPoint


def test_distance_moscow_spb() -> None:
    moscow = GeoPoint(55.7558, 37.6173)
    spb = GeoPoint(59.9311, 30.3609)
    assert moscow.distance_to(spb) == pytest.approx(632, abs=2)


def test_distance_to_itself_is_zero() -> None:
    point = GeoPoint(10, 20)
    assert point.distance_to(point) == pytest.approx(0.0)


def test_out_of_range_is_rejected() -> None:
    with pytest.raises(ValueError):
        GeoPoint(91, 0)
    with pytest.raises(ValueError):
        GeoPoint(0, -181)

from date_factory import Date


def test_formats_round_trip() -> None:
    assert Date.from_iso("2026-03-05").to_iso() == "2026-03-05"
    assert str(Date.from_american("03/05/2026")) == "05.03.2026"


def test_ordering_is_chronological() -> None:
    assert sorted([Date(1, 1, 2027), Date(31, 12, 2026)]) == [
        Date(31, 12, 2026),
        Date(1, 1, 2027),
    ]


def test_validation() -> None:
    import pytest

    with pytest.raises(ValueError):
        Date(32, 1, 2026)

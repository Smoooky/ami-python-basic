from datetime import UTC, date, datetime, timedelta

import pytest
from clock import as_date, as_datetime, between, is_date, is_datetime, order, same_day

DAY = date(2026, 9, 1)
MOMENT = datetime(2026, 9, 1, 10, 30)


def test_is_datetime() -> None:
    assert is_datetime(MOMENT) is True
    assert is_datetime(DAY) is False


def test_is_date_is_not_just_isinstance() -> None:
    assert is_date(DAY) is True
    assert is_date(MOMENT) is False
    # Хотя вот так оно выглядит из isinstance:
    assert isinstance(MOMENT, date) is True


def test_as_datetime() -> None:
    assert as_datetime(DAY) == datetime(2026, 9, 1, 0, 0)
    assert as_datetime(MOMENT) == MOMENT


def test_as_date() -> None:
    assert as_date(MOMENT) == DAY
    assert as_date(DAY) == DAY
    assert is_date(as_date(MOMENT)) is True


def test_same_day() -> None:
    assert same_day(DAY, MOMENT) is True
    assert same_day(MOMENT, datetime(2026, 9, 1, 23, 59)) is True
    assert same_day(DAY, date(2026, 9, 2)) is False


def test_plain_comparison_does_not_work() -> None:
    # Ради этого задача и нужна: сравнение смеси падает, а равенство молча врёт.
    assert (DAY == datetime(2026, 9, 1, 0, 0)) is False
    with pytest.raises(TypeError):
        _ = DAY < MOMENT
    with pytest.raises(TypeError):
        sorted([MOMENT, DAY])


def test_order_sorts_the_mixture() -> None:
    earlier = datetime(2026, 8, 31, 23, 59)
    assert order([MOMENT, DAY, earlier]) == [earlier, DAY, MOMENT]


def test_order_returns_the_same_objects() -> None:
    result = order([MOMENT, DAY])
    assert result[0] is DAY
    assert result[1] is MOMENT


def test_between() -> None:
    assert between(DAY, MOMENT) == timedelta(hours=10, minutes=30)
    assert between(MOMENT, DAY) == timedelta(hours=-10, minutes=-30)
    assert between(DAY, date(2026, 9, 3)) == timedelta(days=2)


def test_rejects_anything_else() -> None:
    for bad in ["2026-09-01", 1, None, timedelta(days=1)]:
        with pytest.raises(TypeError):
            is_date(bad)


def test_rejects_aware_time() -> None:
    with pytest.raises(ValueError):
        is_date(datetime(2026, 9, 1, tzinfo=UTC))
    with pytest.raises(ValueError):
        as_date(datetime(2026, 9, 1, tzinfo=UTC))

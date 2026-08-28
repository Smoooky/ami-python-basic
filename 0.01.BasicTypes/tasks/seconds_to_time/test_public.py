from seconds_to_time import seconds_to_time


def test_zero() -> None:
    assert seconds_to_time(0) == (0, 0, 0)


def test_minute() -> None:
    assert seconds_to_time(60) == (0, 1, 0)


def test_hour_minute_second() -> None:
    assert seconds_to_time(3661) == (1, 1, 1)

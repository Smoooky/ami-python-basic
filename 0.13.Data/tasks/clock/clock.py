from datetime import date, datetime, timedelta

# Полночь: время, которое приписывается дате, когда её приводят к datetime.
MIDNIGHT = datetime.min.time()


def is_datetime(moment: object) -> bool:
    raise NotImplementedError("Implement me")


def is_date(moment: object) -> bool:
    raise NotImplementedError("Implement me")


def as_datetime(moment: date) -> datetime:
    raise NotImplementedError("Implement me")


def as_date(moment: date) -> date:
    raise NotImplementedError("Implement me")


def same_day(first: date, second: date) -> bool:
    raise NotImplementedError("Implement me")


def order(moments: list[date]) -> list[date]:
    raise NotImplementedError("Implement me")


def between(first: date, second: date) -> timedelta:
    raise NotImplementedError("Implement me")

import pytest
from retry import RetryError, retry


def test_succeeds_after_a_few_failures() -> None:
    calls = []

    def flaky() -> str:
        calls.append(1)
        if len(calls) < 3:
            raise ConnectionError("соединение сброшено")
        return "ok"

    assert retry(flaky, attempts=5) == "ok"
    assert len(calls) == 3


def test_gives_up_and_reports_the_cause() -> None:
    def broken() -> None:
        raise ValueError("данные не разобрать")

    with pytest.raises(RetryError) as info:
        retry(broken, attempts=2)

    assert info.value.attempts == 2
    assert str(info.value) == "попытки исчерпаны: 2"
    assert isinstance(info.value.last_error, ValueError)


def test_unlisted_error_is_not_retried() -> None:
    calls = []

    def broken() -> None:
        calls.append(1)
        raise ValueError("данные не разобрать")

    with pytest.raises(ValueError):
        retry(broken, attempts=5, retry_on=(ConnectionError,))

    assert len(calls) == 1


def test_bad_attempts() -> None:
    with pytest.raises(ValueError):
        retry(lambda: None, attempts=0)

import pytest
from rollback import Rollback


def test_changes_stay_after_a_clean_block() -> None:
    config = {"host": "localhost", "port": 80}
    guard = Rollback(config)

    with guard as draft:
        assert draft is config
        draft["port"] = 8080

    assert config == {"host": "localhost", "port": 8080}
    assert guard.committed is True


def test_changes_are_undone_after_an_error() -> None:
    config = {"host": "localhost", "port": 80}
    guard = Rollback(config)

    with pytest.raises(ValueError), guard as draft:
        draft["port"] = 9999
        del draft["host"]
        raise ValueError("порт занят")

    assert config == {"host": "localhost", "port": 80}
    assert guard.committed is False
    assert isinstance(guard.error, ValueError)


def test_suppressed_error_does_not_leave_the_block() -> None:
    config = {"port": 80}
    guard = Rollback(config, suppress=(KeyError,))

    with guard as draft:
        draft["port"] = 1
        raise KeyError("нет такой секции")

    assert config == {"port": 80}
    assert guard.committed is False

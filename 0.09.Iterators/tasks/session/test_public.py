import pytest
from session import Command, run, session, totals


def test_session_starts_only_on_the_first_next() -> None:
    log: list[str] = []
    register = session(log)
    assert log == []
    assert next(register) == 0
    assert log == ["открыт"]


def test_session_adds_up_prices() -> None:
    log: list[str] = []
    register = session(log)
    next(register)
    assert register.send(120) == 120
    assert register.send(80) == 200


def test_payment_finishes_the_session() -> None:
    log: list[str] = []
    register = session(log)
    next(register)
    register.send(120)
    with pytest.raises(StopIteration):
        register.send(None)
    assert log == ["открыт", "оплачен: 120"]


def test_value_error_resets_the_total() -> None:
    log: list[str] = []
    register = session(log)
    next(register)
    register.send(120)
    assert register.throw(ValueError("пересчитайте")) == 0
    assert register.send(50) == 50
    assert log == ["открыт", "пересчёт"]


def test_close_is_recorded() -> None:
    log: list[str] = []
    register = session(log)
    next(register)
    register.send(120)
    register.close()
    assert log == ["открыт", "брошен: 120"]


def test_run() -> None:
    log: list[str] = []
    commands: list[Command] = [120, 80, "оплата"]
    assert run(commands, log) == 200
    assert log == ["открыт", "оплачен: 200"]


def test_run_without_payment_closes_the_register() -> None:
    log: list[str] = []
    assert run([120, 80], log) == 200
    assert log == ["открыт", "брошен: 200"]


def test_totals_closes_the_register_when_abandoned() -> None:
    log: list[str] = []
    walk = totals([10, 20, 30], log)
    assert next(walk) == 10
    assert log == ["открыт"]
    walk.close()
    assert log == ["открыт", "брошен: 10"]

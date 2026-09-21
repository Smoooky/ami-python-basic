from importlib import import_module

orders = import_module("5_orders")


def test_all_unique() -> None:
    assert orders.all_unique(["а", "б", "в"]) is True
    assert orders.all_unique(["а", "б", "а"]) is False
    assert orders.all_unique([]) is True


def test_seen_once() -> None:
    assert orders.seen_once(["б", "а", "б", "в"]) == ["а", "в"]
    assert orders.seen_once(["а", "а"]) == []
    assert orders.seen_once([]) == []


def test_seen_once_keeps_the_input_order() -> None:
    assert orders.seen_once(["в", "а", "б", "а", "в", "б", "г"]) == ["г"]


def test_first_repeat() -> None:
    assert orders.first_repeat(["б", "а", "а", "б"]) == "а"
    assert orders.first_repeat(["а", "а"]) == "а"
    assert orders.first_repeat(["а", "б"]) is None
    assert orders.first_repeat([]) is None

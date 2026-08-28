from registry import Registry


def test_counter_grows() -> None:
    before = Registry.created
    Registry("a")
    Registry("b")
    assert Registry.created == before + 2


def test_items_are_per_instance() -> None:
    a = Registry("a")
    b = Registry("b")
    a.add("x")
    assert a.items == ["x"]
    assert b.items == []


def test_describe() -> None:
    r = Registry("первый")
    r.add("x")
    assert r.describe() == "первый: 1 элементов"

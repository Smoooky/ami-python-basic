import pytest
from roundtrip import as_key, key_conflicts, restored, survives


def test_as_key_on_strings() -> None:
    assert as_key("имя") == "имя"
    assert as_key("") == ""
    assert as_key("1") == "1"


def test_as_key_on_numbers() -> None:
    assert as_key(1) == "1"
    assert as_key(-3) == "-3"
    assert as_key(10**20) == "100000000000000000000"
    assert as_key(1.5) == "1.5"
    assert as_key(2.0) == "2.0"


def test_as_key_on_named_values() -> None:
    assert as_key(True) == "true"
    assert as_key(False) == "false"
    assert as_key(None) == "null"


def test_as_key_rejects_the_rest() -> None:
    with pytest.raises(TypeError):
        as_key((1, 2))
    with pytest.raises(TypeError):
        as_key(frozenset())
    with pytest.raises(ValueError):
        as_key(float("nan"))


def test_key_conflicts() -> None:
    assert key_conflicts({"a": 1, "b": 2}) == []
    assert key_conflicts({}) == []
    assert key_conflicts({1: "a", "1": "b"}) == ["1"]
    assert key_conflicts({True: "a", "true": "b"}) == ["true"]
    assert key_conflicts({None: "a", "null": "b"}) == ["null"]


def test_key_conflicts_are_sorted() -> None:
    mapping: dict[object, object] = {1: "a", "1": "b", 2: "c", "2": "d"}
    assert key_conflicts(mapping) == ["1", "2"]


def test_restored() -> None:
    assert restored([1, 2]) == [1, 2]
    assert restored({"a": 1}) == {"a": 1}
    assert restored((1, 2)) == [1, 2]
    assert restored({1: "a"}) == {"1": "a"}


def test_survives_the_plain_values() -> None:
    values: list[object] = [None, True, False, 0, -3, 2.5, 10**30, "текст", [], {}, [1, "a"]]
    for value in values:
        assert survives(value) is True


def test_does_not_survive() -> None:
    assert survives((1, 2)) is False
    assert survives({1: "a"}) is False
    assert survives(float("nan")) is False
    assert survives({1, 2}) is False


def test_a_loop_does_not_survive_either() -> None:
    loop: list[object] = [1]
    loop.append(loop)
    assert survives(loop) is False

from invert_dict import invert_dict


def test_simple() -> None:
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_empty() -> None:
    assert invert_dict({}) == {}


def test_duplicate_values() -> None:
    assert invert_dict({"x": 1, "y": 1}) == {1: "y"}

from bind_arguments import bind_arguments

PARAMETERS = [("x", "p"), ("y", "n"), ("z", "k")]


def test_positional_fill() -> None:
    assert bind_arguments(PARAMETERS, {"z": 0}, [1, 2], {}) == {"x": 1, "y": 2, "z": 0}


def test_keyword_fill() -> None:
    assert bind_arguments(PARAMETERS, {"z": 0}, [1], {"y": 5, "z": 9}) == {"x": 1, "y": 5, "z": 9}


def test_only_defaults() -> None:
    assert bind_arguments([("a", "n")], {"a": 42}, [], {}) == {"a": 42}

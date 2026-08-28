from hello_world import greet


def test_simple() -> None:
    assert greet("world") == "Hello, world!"


def test_empty_name() -> None:
    assert greet("") == "Hello, !"


def test_returns_str() -> None:
    assert isinstance(greet("x"), str)

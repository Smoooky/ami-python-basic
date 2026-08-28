from about import annotations_of, is_annotated, name_of, returns


def double(x: int) -> int:
    return x * 2


def greet(name: str, loud: bool) -> str:
    return name.upper() if loud else name


def bare(x, y):  # type: ignore[no-untyped-def]
    return x


def silent(x: int) -> None:
    return None


def test_name_of() -> None:
    assert name_of(double) == "double"
    assert name_of(greet) == "greet"


def test_name_of_a_lambda() -> None:
    assert name_of(lambda x: x) == "<lambda>"


def test_is_annotated() -> None:
    assert is_annotated(double) is True
    assert is_annotated(bare) is False


def test_annotations_of() -> None:
    assert annotations_of(double) == {"x": "int", "return": "int"}
    assert annotations_of(greet) == {"name": "str", "loud": "bool", "return": "str"}


def test_annotations_of_an_unannotated_function() -> None:
    assert annotations_of(bare) == {}


def test_annotations_of_a_none_returning_function() -> None:
    assert annotations_of(silent) == {"x": "int", "return": "NoneType"}


def test_returns() -> None:
    assert returns(double) == "int"
    assert returns(greet) == "str"
    assert returns(bare) == ""


def test_returns_none_is_a_type_too() -> None:
    # У None-результата тип называется NoneType.
    assert returns(silent) == "NoneType"


def test_returns_of_a_lambda() -> None:
    assert returns(lambda x: x) == ""

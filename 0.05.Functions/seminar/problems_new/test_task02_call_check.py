from task02_call_check import bind, kind_of, problems_of

# def f(x, /, y, *, z=0) в табличном виде
XYZ = [("x", "p"), ("y", "n"), ("z", "k")]


def test_kind_of_basic() -> None:
    params = [("a", "p"), ("b", "n"), ("c", "k")]
    assert kind_of(params, "a") == "p"
    assert kind_of(params, "b") == "n"
    assert kind_of(params, "c") == "k"


def test_kind_of_unknown_name() -> None:
    assert kind_of([("a", "n")], "b") == ""
    assert kind_of([], "a") == ""


def test_bind_positional_and_keyword() -> None:
    assert bind(XYZ, {"z"}, (1, 2), {"z": 3}) == {"x": 1, "y": 2, "z": 3}


def test_bind_all_by_keyword() -> None:
    params = [("a", "n"), ("b", "k")]
    assert bind(params, set(), (), {"a": 1, "b": 2}) == {"a": 1, "b": 2}


def test_bind_does_not_fill_defaults() -> None:
    # Главная проверка: дефолт z не подставляется — передано только x и y.
    assert bind(XYZ, {"z"}, (1, 2), {}) == {"x": 1, "y": 2}


def test_problems_of_correct_calls_are_empty() -> None:
    assert problems_of(XYZ, {"z"}, (1, 2), {"z": 3}) == []
    assert problems_of(XYZ, {"z"}, (1, 2), {}) == []
    assert problems_of([("a", "n")], set(), (), {"a": 1}) == []


def test_problems_of_extra_positional() -> None:
    assert problems_of([("a", "n")], set(), (1, 2), {}) == ["лишний позиционный аргумент"]


def test_problems_of_keyword_for_positional_only() -> None:
    assert problems_of(XYZ, {"z"}, (1, 2), {"x": 0}) == [
        "параметр 'x' только позиционный, а передан по имени"
    ]


def test_problems_of_multiple_values() -> None:
    assert problems_of([("a", "n")], set(), (1,), {"a": 2}) == [
        "несколько значений для параметра 'a'"
    ]


def test_problems_of_unexpected_keyword() -> None:
    assert problems_of([("a", "n")], set(), (1,), {"w": 0}) == [
        "неожидаемый именованный аргумент 'w'"
    ]


def test_problems_of_missing_value() -> None:
    assert problems_of([("a", "n"), ("b", "n")], set(), (1,), {}) == [
        "нет значения для параметра 'b'"
    ]
    assert problems_of([("a", "n")], set(), (), {}) == ["нет значения для параметра 'a'"]


def test_problems_of_message_order() -> None:
    # Главная проверка: порядок фиксирован — правило 2, затем 4, затем 5.
    got = problems_of(XYZ, {"z"}, (1,), {"x": 0, "w": 5})
    assert got == [
        "параметр 'x' только позиционный, а передан по имени",
        "неожидаемый именованный аргумент 'w'",
        "нет значения для параметра 'y'",
    ]

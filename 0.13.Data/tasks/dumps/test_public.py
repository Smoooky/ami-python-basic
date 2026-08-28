import json

import pytest
from dumps import dump_string, dumps, dumps_sorted


def test_scalars() -> None:
    assert dumps(None) == "null"
    assert dumps(True) == "true"
    assert dumps(False) == "false"
    assert dumps(0) == "0"
    assert dumps(-12) == "-12"
    assert dumps(3.5) == "3.5"


def test_true_is_not_one() -> None:
    # isinstance(True, int) — правда, поэтому порядок проверок решает всё.
    assert dumps(True) == "true"
    assert dumps([1, True, 0, False]) == "[1, true, 0, false]"
    assert dumps({"а": True}) == '{"а": true}'


def test_strings() -> None:
    assert dump_string("текст") == '"текст"'
    assert dump_string("") == '""'
    assert dump_string('он сказал "да"') == '"он сказал \\"да\\""'
    assert dump_string("две\nстроки") == '"две\\nстроки"'
    assert dump_string("слеш \\ внутри") == '"слеш \\\\ внутри"'


def test_cyrillic_stays_readable() -> None:
    assert dumps("Отчёт") == '"Отчёт"'
    assert dumps({"тема": "тёмная"}) == '{"тема": "тёмная"}'


def test_containers() -> None:
    assert dumps([]) == "[]"
    assert dumps({}) == "{}"
    assert dumps([1, 2, 3]) == "[1, 2, 3]"
    assert dumps({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'
    assert dumps({"a": [1, {"b": None}]}) == '{"a": [1, {"b": null}]}'


def test_key_order_is_the_dict_order() -> None:
    assert dumps({"б": 1, "а": 2}) == '{"б": 1, "а": 2}'
    assert dumps_sorted({"б": 1, "а": 2}) == '{"а": 2, "б": 1}'
    assert dumps_sorted({"b": {"z": 1, "y": 2}}) == '{"b": {"y": 2, "z": 1}}'


def test_matches_the_json_module() -> None:
    values: list[object] = [
        None,
        [1, 2.5, "текст", True, None],
        {"имя": "Иванов", "теги": ["a", "b"], "есть": False},
        {"вложено": {"глубже": {"ещё": [1, [2, [3]]]}}},
    ]
    for value in values:
        assert dumps(value) == json.dumps(value, ensure_ascii=False)
        assert dumps_sorted(value) == json.dumps(value, ensure_ascii=False, sort_keys=True)


def test_rejects_what_json_has_no_place_for() -> None:
    with pytest.raises(TypeError):
        dumps({1: "a"})
    with pytest.raises(TypeError):
        dumps((1, 2))
    with pytest.raises(TypeError):
        dumps({1, 2})
    with pytest.raises(ValueError):
        dumps(float("nan"))
    with pytest.raises(ValueError):
        dumps(float("inf"))


def test_rejects_a_loop() -> None:
    loop: list[object] = [1]
    loop.append(loop)
    with pytest.raises(ValueError):
        dumps(loop)


def test_the_same_object_twice_is_not_a_loop() -> None:
    shared = [1, 2]
    assert dumps([shared, shared]) == "[[1, 2], [1, 2]]"

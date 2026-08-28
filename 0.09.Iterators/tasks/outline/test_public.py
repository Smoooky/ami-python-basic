import inspect

from outline import Item, chain, depth, flat, numbered

PLAN: list[Item] = [
    "Введение",
    [
        "Что такое итератор",
        ["Протокол", "Примеры"],
    ],
    "Заключение",
]


def test_flat() -> None:
    assert list(flat(PLAN)) == [
        "Введение",
        "Что такое итератор",
        "Протокол",
        "Примеры",
        "Заключение",
    ]
    assert list(flat(["один"])) == ["один"]
    assert list(flat([])) == []


def test_numbered() -> None:
    assert list(numbered(PLAN)) == [
        (0, "Введение"),
        (1, "Что такое итератор"),
        (2, "Протокол"),
        (2, "Примеры"),
        (0, "Заключение"),
    ]


def test_depth() -> None:
    assert depth([]) == 0
    assert depth(["а", "б"]) == 1
    assert depth(["а", ["б"]]) == 2
    assert depth(PLAN) == 3


def test_chain() -> None:
    assert list(chain([1, 2], [3], [])) == [1, 2, 3]
    assert list(chain()) == []
    assert list(chain("аб", [1])) == ["а", "б", 1]


def test_flat_and_chain_are_generators() -> None:
    assert inspect.isgenerator(flat(PLAN))
    assert inspect.isgenerator(numbered(PLAN))
    assert inspect.isgenerator(chain([1], [2]))

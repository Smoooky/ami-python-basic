from typing import Any

import pytest
from tags import Tags


def test_creation_and_normalization() -> None:
    assert Tags.normalize("  Бег  ") == "бег"

    anya = Tags("Питон", "Бег", "  настолки  ")
    assert len(anya) == 3
    assert "ПИТОН" in anya
    not_a_tag: Any = 42
    assert (not_a_tag in anya) is False
    assert repr(anya) == "Tags('бег', 'настолки', 'питон')"

    assert Tags("бег", "БЕГ", "  бег  ") == Tags("бег")
    with pytest.raises(ValueError):
        Tags("Питон", "")


def test_set_operations_come_for_free() -> None:
    anya = Tags("Питон", "Бег", "настолки")
    borya = Tags("Питон", "гитара")

    assert anya & borya == Tags("питон")
    assert anya | borya == Tags("бег", "гитара", "настолки", "питон")
    assert anya - borya == Tags("бег", "настолки")
    assert anya ^ borya == Tags("бег", "гитара", "настолки")


def test_operations_return_tags() -> None:
    anya = Tags("бег", "питон")
    borya = Tags("питон", "гитара")
    for result in (anya & borya, anya | borya, anya - borya, anya ^ borya):
        assert isinstance(result, Tags)


def test_comparisons_and_hashing() -> None:
    anya = Tags("питон", "бег", "настолки")

    assert Tags("питон") <= anya
    assert (anya <= Tags("питон")) is False
    assert anya.isdisjoint(Tags("вязание")) is True

    assert Tags.of(["Питон", "Бег"]) == anya & Tags("питон", "бег")
    assert len({Tags("бег"), Tags("БЕГ")}) == 1
    assert {anya: "Аня"}[Tags("настолки", "питон", "бег")] == "Аня"

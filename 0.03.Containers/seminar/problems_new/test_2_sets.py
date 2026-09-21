from importlib import import_module

sets = import_module("2_sets")


def test_either() -> None:
    assert sets.either(["а", "б"], ["б", "в"]) == ["а", "б", "в"]
    assert sets.either(["б", "а"], ["а"]) == ["а", "б"]
    assert sets.either([], ["в", "б"]) == ["б", "в"]


def test_either_drops_duplicates() -> None:
    assert sets.either(["а", "а"], ["а"]) == ["а"]


def test_common_to_all() -> None:
    assert sets.common_to_all([["а", "б"], ["б", "в", "а"]]) == ["а", "б"]
    assert sets.common_to_all([["а"], ["б"]]) == []
    assert sets.common_to_all([["а", "а"]]) == ["а"]


def test_common_to_all_with_no_lists() -> None:
    assert sets.common_to_all([]) == []


def test_no_overlap() -> None:
    assert sets.no_overlap(["а", "б"], ["в", "г"]) is True
    assert sets.no_overlap(["а"], ["а", "б"]) is False
    assert sets.no_overlap([], ["а"]) is True


def test_same_members() -> None:
    assert sets.same_members(["а", "б", "а"], ["б", "а"]) is True
    assert sets.same_members(["а"], ["б"]) is False
    assert sets.same_members([], []) is True
    assert sets.same_members(["а"], []) is False

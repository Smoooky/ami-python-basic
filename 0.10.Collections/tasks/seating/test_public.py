import pytest
from seating import codes, menus, photos, scoops, teams


def test_menus() -> None:
    assert menus(["борщ", "уха"], ["плов", "котлета"]) == [
        ("борщ", "плов"),
        ("борщ", "котлета"),
        ("уха", "плов"),
        ("уха", "котлета"),
    ]
    assert menus([], ["плов"]) == []


def test_codes() -> None:
    assert codes("01", 2) == ["00", "01", "10", "11"]
    assert codes("абв", 1) == ["а", "б", "в"]
    assert len(codes("0123456789", 3)) == 1000


def test_photos() -> None:
    assert photos(["Аня", "Боря"]) == [("Аня", "Боря"), ("Боря", "Аня")]
    assert len(photos(["а", "б", "в", "г"])) == 24
    assert photos([]) == [()]


def test_teams() -> None:
    assert teams(["Аня", "Боря", "Вера"], 2) == [
        ("Аня", "Боря"),
        ("Аня", "Вера"),
        ("Боря", "Вера"),
    ]
    assert teams(["Аня", "Боря"], 3) == []


def test_scoops() -> None:
    assert scoops(["ваниль", "шоколад"], 2) == [
        ("ваниль", "ваниль"),
        ("ваниль", "шоколад"),
        ("шоколад", "шоколад"),
    ]
    assert len(scoops(["а", "б", "в"], 2)) == 6


def test_arguments_are_checked() -> None:
    with pytest.raises(ValueError):
        codes("аб", -1)
    with pytest.raises(ValueError):
        teams(["а"], -1)
    with pytest.raises(ValueError):
        scoops(["а"], -1)

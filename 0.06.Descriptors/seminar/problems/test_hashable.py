from hashable import Coord, unique


def test_equal_points() -> None:
    assert Coord(1, 2) == Coord(1, 2)
    assert Coord(1, 2) != Coord(1, 3)


def test_comparison_with_another_type() -> None:
    # Не ошибка, а False: сравнивать можно с чем угодно.
    assert (Coord(1, 2) == "не точка") is False


def test_point_is_hashable() -> None:
    assert isinstance(hash(Coord(1, 2)), int)


def test_equal_points_have_equal_hashes() -> None:
    # Без этого множество не схлопнет одинаковые точки.
    assert hash(Coord(1, 2)) == hash(Coord(1, 2))


def test_point_works_in_a_set() -> None:
    assert len({Coord(1, 2), Coord(1, 2), Coord(3, 4)}) == 2


def test_point_works_as_a_dict_key() -> None:
    distances = {Coord(0, 0): "начало"}
    assert distances[Coord(0, 0)] == "начало"


def test_unique() -> None:
    assert unique([Coord(1, 2), Coord(1, 2), Coord(3, 4)]) == 2
    assert unique([]) == 0
    assert unique([Coord(0, 0)]) == 1

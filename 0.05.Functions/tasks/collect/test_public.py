from collect import collect


def test_creates_new_list() -> None:
    assert collect(1) == [1]


def test_calls_are_independent() -> None:
    assert collect(1) == [1]
    assert collect(2) == [2]


def test_appends_to_given_list() -> None:
    assert collect(3, [1, 2]) == [1, 2, 3]

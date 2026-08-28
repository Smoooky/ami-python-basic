from group_by_length import group_by_length


def test_simple() -> None:
    assert group_by_length(["кот", "дом", "море"]) == {3: ["кот", "дом"], 4: ["море"]}


def test_repeats_are_kept() -> None:
    assert group_by_length(["a", "b", "a"]) == {1: ["a", "b", "a"]}


def test_empty() -> None:
    assert group_by_length([]) == {}

from hash_table import hash_table


def test_two_buckets() -> None:
    assert hash_table([(1, "a"), (2, "b")], 2) == [[(2, "b")], [(1, "a")]]


def test_collision_keeps_both() -> None:
    assert hash_table([(1, "a"), (3, "b")], 2) == [[], [(1, "a"), (3, "b")]]


def test_update_does_not_add_second_pair() -> None:
    assert hash_table([(1, "a"), (1, "b")], 2) == [[], [(1, "b")]]

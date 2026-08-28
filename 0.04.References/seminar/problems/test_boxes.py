from boxes import add_to_slot, frozen_copy, replace_slot


def test_add_to_slot() -> None:
    box: tuple[list[int], ...] = ([], [7])
    add_to_slot(box, 0, 1)
    assert box == ([1], [7])


def test_add_to_slot_keeps_the_same_tuple_and_list() -> None:
    inner: list[int] = []
    box = (inner,)
    add_to_slot(box, 0, 5)
    assert box[0] is inner
    assert inner == [5]


def test_add_to_slot_twice() -> None:
    box: tuple[list[int], ...] = ([],)
    add_to_slot(box, 0, 1)
    add_to_slot(box, 0, 2)
    assert box == ([1, 2],)


def test_replace_slot() -> None:
    assert replace_slot((1, 2, 3), 1, 9) == (1, 9, 3)
    assert replace_slot((1,), 0, 0) == (0,)


def test_replace_slot_returns_a_new_tuple() -> None:
    box = (1, 2, 3)
    result = replace_slot(box, 0, 9)
    assert box == (1, 2, 3)
    assert result is not box


def test_replace_slot_at_the_end() -> None:
    assert replace_slot((1, 2, 3), 2, 9) == (1, 2, 9)


def test_frozen_copy() -> None:
    assert frozen_copy(([1, 2], [3])) == ((1, 2), (3,))
    assert frozen_copy(()) == ()
    assert frozen_copy(([],)) == ((),)


def test_frozen_copy_does_not_share_data_with_the_source() -> None:
    inner = [1, 2]
    result = frozen_copy((inner,))
    inner.append(3)
    assert result == ((1, 2),)


def test_frozen_copy_result_is_hashable() -> None:
    # У кортежа из кортежей есть хеш, значит внутри нет изменяемых объектов.
    assert hash(frozen_copy(([1, 2],))) == hash(((1, 2),))

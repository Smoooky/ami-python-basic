from duck_check import abc_names, hash_promise_broken, is_hashable, looks_like


def test_looks_like() -> None:
    assert looks_like([1, 2], "__len__", "__getitem__") is True
    assert looks_like([1, 2], "__len__", "keys") is False
    assert looks_like(42) is True


def test_is_hashable() -> None:
    assert is_hashable("строка") is True
    assert is_hashable(42) is True
    assert is_hashable((1, 2)) is True
    assert is_hashable([1, 2]) is False
    assert is_hashable((1, 2, [3, 4])) is False


def test_abc_names() -> None:
    assert abc_names([1, 2]) == {"Sized", "Iterable", "Container", "Sequence", "MutableSequence"}
    assert abc_names("строка") == {"Sized", "Iterable", "Container", "Hashable", "Sequence"}
    assert abc_names(42) == {"Hashable"}
    assert abc_names(print) == {"Hashable", "Callable"}


def test_hash_promise_broken() -> None:
    assert hash_promise_broken((1, 2, [3, 4])) is True
    assert hash_promise_broken((1, 2, 3)) is False
    assert hash_promise_broken([1, 2]) is False

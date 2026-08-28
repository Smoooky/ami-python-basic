from deep_copy import deep_copy


def test_nested_list_is_independent() -> None:
    original = [1, [2, 3]]
    copy = deep_copy(original)
    copy[1].append(4)
    assert original == [1, [2, 3]]


def test_shared_reference_is_preserved() -> None:
    shared = [0]
    result = deep_copy([shared, shared])
    assert result[0] is result[1]
    assert result[0] is not shared


def test_scalars_are_returned_as_is() -> None:
    assert deep_copy(5) == 5
    assert deep_copy("text") == "text"
    assert deep_copy(None) is None

from keys import distinct_count, same_key, surviving_type


def test_same_key_for_equal_numbers() -> None:
    assert same_key(1, True) is True
    assert same_key(1, 1.0) is True
    assert same_key(0, False) is True


def test_same_key_for_different_numbers() -> None:
    assert same_key(1, 2) is False
    assert same_key(1, 1.5) is False
    assert same_key(0, 1) is False


def test_surviving_type_keeps_the_first_key() -> None:
    assert surviving_type(1, True) == "int"
    assert surviving_type(True, 1) == "bool"
    assert surviving_type(1.0, 1) == "float"


def test_surviving_type_when_values_differ() -> None:
    assert surviving_type(1, 2) == "int"
    assert surviving_type(True, 5) == "bool"


def test_distinct_count() -> None:
    assert distinct_count([1, True, 1.0, 2]) == 2
    assert distinct_count([0, False]) == 1
    assert distinct_count([1, 2, 3]) == 3
    assert distinct_count([]) == 0

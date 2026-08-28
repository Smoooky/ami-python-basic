from bits import clear_bit, is_power_of_two, nth_bit, set_bit


def test_nth_bit() -> None:
    assert nth_bit(5, 0) == 1
    assert nth_bit(5, 1) == 0
    assert nth_bit(5, 2) == 1
    assert nth_bit(5, 3) == 0
    assert nth_bit(0, 0) == 0


def test_nth_bit_far_from_the_number() -> None:
    assert nth_bit(5, 100) == 0
    assert nth_bit(2**100, 100) == 1


def test_set_bit() -> None:
    assert set_bit(0, 0) == 1
    assert set_bit(0, 3) == 8
    assert set_bit(5, 1) == 7


def test_set_bit_is_idempotent() -> None:
    assert set_bit(5, 0) == 5
    assert set_bit(set_bit(0, 4), 4) == 16


def test_clear_bit() -> None:
    assert clear_bit(5, 0) == 4
    assert clear_bit(5, 2) == 1
    assert clear_bit(255, 7) == 127


def test_clear_bit_of_an_already_zero_bit() -> None:
    assert clear_bit(5, 1) == 5
    assert clear_bit(0, 10) == 0


def test_set_and_clear_are_opposite() -> None:
    assert clear_bit(set_bit(40, 2), 2) == 40


def test_is_power_of_two() -> None:
    assert is_power_of_two(1) is True
    assert is_power_of_two(2) is True
    assert is_power_of_two(1024) is True
    assert is_power_of_two(2**100) is True


def test_is_not_power_of_two() -> None:
    assert is_power_of_two(0) is False
    assert is_power_of_two(3) is False
    assert is_power_of_two(1023) is False
    assert is_power_of_two(2**100 + 1) is False

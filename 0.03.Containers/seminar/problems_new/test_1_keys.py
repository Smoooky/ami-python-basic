from importlib import import_module

keys = import_module("1_keys")


def test_same_hash_for_equal_values() -> None:
    assert keys.same_hash(1, True) is True
    assert keys.same_hash(1, 1.0) is True
    assert keys.same_hash(0, False) is True


def test_same_hash_for_different_values() -> None:
    assert keys.same_hash(1, 2) is False
    assert keys.same_hash(1, 1.5) is False


def test_collide_only() -> None:
    P = 2**61 - 1
    assert keys.collide_only(0, P) is True
    assert keys.collide_only(P, 0) is True
    assert keys.collide_only(1, P + 1) is True
    assert keys.collide_only(2 * P, P) is True


def test_collide_only_is_not_about_equal_keys() -> None:
    assert keys.collide_only(1, 1) is False
    assert keys.collide_only(1, 2) is False


def test_who_stayed() -> None:
    assert keys.who_stayed([(1.0, "а"), (True, "б"), (1, "в")]) == ("float", "в")
    assert keys.who_stayed([(0, "а")]) == ("int", "а")
    assert keys.who_stayed([(False, "а"), (0.0, "б")]) == ("bool", "б")

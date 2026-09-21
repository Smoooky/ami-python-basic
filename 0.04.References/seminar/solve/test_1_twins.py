from importlib import import_module

twins = import_module("1_twins")


def test_fresh_int_gives_a_new_object() -> None:
    first = twins.fresh_int(1000)
    second = twins.fresh_int(1000)

    assert first == second
    assert first is not second


def test_fresh_int_cannot_escape_the_cache() -> None:
    assert twins.fresh_int(5) is twins.fresh_int(5)
    assert twins.fresh_int(256) is twins.fresh_int(256)


def test_fresh_copy_equals_but_distinct() -> None:
    word = "hello"

    first = twins.fresh_copy(word)
    second = twins.fresh_copy(word)

    assert first == word
    assert first is not word
    assert first is not second


def test_fresh_copy_of_a_short_word() -> None:
    first = twins.fresh_copy("ab")
    second = twins.fresh_copy("ab")

    assert first == "ab"
    assert first is not second


def test_cached_detects_the_small_int_cache() -> None:
    assert twins.cached(0) is True
    assert twins.cached(5) is True
    assert twins.cached(256) is True
    assert twins.cached(257) is False
    assert twins.cached(1000) is False

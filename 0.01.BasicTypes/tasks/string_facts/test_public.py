from string_facts import string_facts


def test_simple_word() -> None:
    assert string_facts("hello") == (5, 0, "HELLO")


def test_with_spaces() -> None:
    assert string_facts("a b c") == (5, 2, "A B C")


def test_empty() -> None:
    assert string_facts("") == (0, 0, "")

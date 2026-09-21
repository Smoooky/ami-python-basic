from importlib import import_module

recursion = import_module("3_recursion")


def test_digits_sum() -> None:
    assert recursion.digits_sum(0) == 0
    assert recursion.digits_sum(7) == 7
    assert recursion.digits_sum(12345) == 15


def test_is_palindrome() -> None:
    assert recursion.is_palindrome("") is True
    assert recursion.is_palindrome("а") is True
    assert recursion.is_palindrome("кок") is True
    assert recursion.is_palindrome("абба") is True
    assert recursion.is_palindrome("кот") is False


def test_is_palindrome_is_case_sensitive() -> None:
    assert recursion.is_palindrome("Анна") is False


def test_reverse_items() -> None:
    assert recursion.reverse_items([]) == []
    assert recursion.reverse_items([1]) == [1]
    assert recursion.reverse_items([1, 2, 3]) == [3, 2, 1]


def test_reverse_items_does_not_touch_the_input() -> None:
    items = [1, 2, 3]

    result = recursion.reverse_items(items)

    assert result is not items
    assert items == [1, 2, 3]


def test_mutual_even_and_odd() -> None:
    for n in range(6):
        assert recursion.is_even_rec(n) is (n % 2 == 0)
        assert recursion.is_odd_rec(n) is (n % 2 == 1)

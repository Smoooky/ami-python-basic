"""Решение задачи 3 (problems_new/3_recursion.py)."""


def digits_sum(n: int) -> int:
    """База — однозначное число; шаг — последняя цифра плюс хвост."""
    if n < 10:
        return n
    return n % 10 + digits_sum(n // 10)


def is_palindrome(text: str) -> bool:
    """Крайние символы равны и середина — палиндром."""
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])


def reverse_items(items: list[int]) -> list[int]:
    """Развёрнутый хвост плюс первый элемент в конце."""
    if not items:
        return []
    return reverse_items(items[1:]) + items[:1]


def is_even_rec(n: int) -> bool:
    """Ноль чётный; дальше чётность каждый шаг меняется на противоположную."""
    if n == 0:
        return True
    return is_odd_rec(n - 1)


def is_odd_rec(n: int) -> bool:
    """Ноль нечётным не бывает."""
    if n == 0:
        return False
    return is_even_rec(n - 1)

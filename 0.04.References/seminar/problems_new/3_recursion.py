"""Задача 3. Спуск и база.

Каждая функция ниже решается рекурсией: базовый случай останавливает спуск,
шаг уменьшает задачу. Циклы писать не запрещено, но интереснее без них.
Числа на входе неотрицательные.
"""


def digits_sum(n: int) -> int:
    """Сумма цифр неотрицательного числа.

    База — однозначное число: оно само себе сумма. Шаг — последняя цифра
    плюс сумма цифр всего остального.
    """
    raise NotImplementedError("Implement me")


def is_palindrome(text: str) -> bool:
    """Читается ли строка одинаково в обе стороны. Регистр важен.

    База — строка из нуля или одного символа. Шаг — сравнить крайние
    символы и задать тот же вопрос середине.
    """
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])
    raise NotImplementedError("Implement me")


def reverse_items(items: list[int]) -> list[int]:
    """Новый список в обратном порядке. Исходный не меняется.

    База — пустой список. Шаг — рекурсивно развёрнутый хвост плюс первый
    элемент в конце.
    """
    raise NotImplementedError("Implement me")


def is_even_rec(n: int) -> bool:
    """Чётное ли число. Отвечает взаимной рекурсией с is_odd_rec.

    База: ноль чётный. Шаг: n чётно ровно тогда, когда n - 1 нечётно.
    """
    raise NotImplementedError("Implement me")


def is_odd_rec(n: int) -> bool:
    """Нечётное ли число. База: ноль нечётным не бывает."""
    raise NotImplementedError("Implement me")

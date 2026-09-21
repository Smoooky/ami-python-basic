"""Задача 4. Словарь как группировщик — второй заход.

Готовые инструменты (defaultdict, Counter) — лекция 10; здесь всё собирается
руками: `setdefault` для списков-групп и `get` для счётчиков.
"""


def by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Слова, сгруппированные по первой букве.

    Пустых строк в списке нет. Порядок слов внутри группы — как во входном
    списке, повторы сохраняются.
    """
    raise NotImplementedError("Implement me")


def word_counts(text: str) -> dict[str, int]:
    """Сколько раз каждое слово встречается в строке.

    Слова — части, разделённые пробелами (`split`). Регистр учитывается.
    """
    raise NotImplementedError("Implement me")


def keys_by_value(mapping: dict[str, int]) -> dict[int, list[str]]:
    """Ключи исходного словаря, сгруппированные по значениям.

    Порядок ключей внутри группы — как в исходном словаре.
    """
    raise NotImplementedError("Implement me")

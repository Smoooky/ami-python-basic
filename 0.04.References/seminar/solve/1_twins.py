"""Решение задачи 1 (problems_new/1_twins.py)."""


def fresh_int(n: int) -> int:
    """Разбор строки происходит в рантайме — кэш маленьких чисел не работает."""
    return int(str(n))


def fresh_copy(word: str) -> str:
    """Конкатенация выделяет новую строку, срез-подстрока — тоже."""
    return (word + " ")[:-1]


def cached(n: int) -> bool:
    """Заново собранное число совпадает личностью только с объектом из кэша."""
    return int(str(n)) is n

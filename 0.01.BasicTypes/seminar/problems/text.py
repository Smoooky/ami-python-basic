"""Задача 4. Текст: кодовые точки, байты и нормализация.

Пригодятся ord, len, str.encode, str.casefold и unicodedata.normalize. Функцию
map из лекции здесь тоже удобно применить.
"""


def codepoints(text: str) -> tuple[int, ...]:
    """Номера кодовых точек всех символов строки: "AB" -> (65, 66)."""
    raise NotImplementedError("Implement me")


def byte_size(text: str, encoding: str) -> int:
    """Сколько байт занимает строка в указанной кодировке.

    byte_size("ы", "utf-8") == 2, byte_size("ы", "cp1251") == 1.
    """
    raise NotImplementedError("Implement me")


def canonical(text: str) -> str:
    """Приведение текста к сравнимому виду: убрать пробелы по краям, привести
    к нормальной форме NFC, свернуть регистр через casefold.

    Порядок шагов именно такой.
    """
    raise NotImplementedError("Implement me")


def same_text(first: str, second: str) -> bool:
    """Один ли это текст с точки зрения человека: регистр, пробелы по краям и
    форма записи букв с диакритикой не учитываются."""
    raise NotImplementedError("Implement me")

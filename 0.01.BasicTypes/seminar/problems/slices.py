"""Задача 3. Срезы.

Каждая функция — один срез или пара срезов. Ни одна не имеет права упасть на
пустой строке или на слишком большом аргументе: срез за границами строки
ошибки не даёт.
"""


def reverse(text: str) -> str:
    """Строка задом наперёд."""
    raise NotImplementedError("Implement me")


def every_other(text: str) -> str:
    """Каждый второй символ, считая с первого: "абвгд" -> "авд"."""
    raise NotImplementedError("Implement me")


def head(text: str, n: int) -> str:
    """Первые n символов. Если строка короче — вся строка целиком."""
    raise NotImplementedError("Implement me")


def trim(text: str, k: int) -> str:
    """Строка без k символов с каждого края: trim("привет", 1) -> "риве".

    При k == 0 возвращается вся строка. Запись text[k:-k] здесь не работает:
    -0 — это 0, и срез выйдет пустым.
    """
    raise NotImplementedError("Implement me")


def swap_halves(text: str) -> str:
    """Половины строки меняются местами: "абвгде" -> "гдеабв".

    При нечётной длине середина считается частью второй половины:
    "абвгд" -> "вгдаб".
    """
    raise NotImplementedError("Implement me")

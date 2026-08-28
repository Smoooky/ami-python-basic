"""Задача 1. Значения по умолчанию и границы.

Разница между «значение пустое» и «значения нет» здесь принципиальна: ноль и
пустая строка — полноценные значения, а `None` означает отсутствие.
"""


def label(name: str) -> str:
    """Имя для вывода. Пустая строка заменяется на "аноним"."""
    raise NotImplementedError("Implement me")


def setting(value: int | None, default: int) -> int:
    """Значение настройки: если значения нет, берётся default.

    Ноль — допустимое значение и заменяться не должен.
    """
    raise NotImplementedError("Implement me")


def first_filled(values: list[str], default: str) -> str:
    """Первая непустая строка списка. Если таких нет — default."""
    raise NotImplementedError("Implement me")


def clamp(value: int, low: int, high: int) -> int:
    """Значение, прижатое к границам отрезка: меньше low становится low, больше
    high — high. Границы задаются в правильном порядке."""
    raise NotImplementedError("Implement me")

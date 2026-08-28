"""Задача 4. Стопка значений.

Стопка отдаёт значения в обратном порядке: последнее положенное снимается
первым. Исключения мы ещё не проходили, поэтому на пустой стопке методы
возвращают None, а не сообщают об ошибке.
"""


class Stack:
    """Стопка целых чисел."""

    def __init__(self) -> None:
        """Пустая стопка."""
        raise NotImplementedError("Implement me")

    def push(self, value: int) -> None:
        """Положить значение наверх."""
        raise NotImplementedError("Implement me")

    def pop(self) -> int | None:
        """Снять верхнее значение и вернуть его. На пустой стопке — None."""
        raise NotImplementedError("Implement me")

    def peek(self) -> int | None:
        """Посмотреть верхнее значение, не снимая. На пустой стопке — None."""
        raise NotImplementedError("Implement me")

    def size(self) -> int:
        """Сколько значений в стопке."""
        raise NotImplementedError("Implement me")

    def is_empty(self) -> bool:
        """Пуста ли стопка."""
        raise NotImplementedError("Implement me")

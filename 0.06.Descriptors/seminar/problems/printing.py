"""Задача 1. Два способа показать объект.

`__repr__` пишут для того, кто отлаживает код: по нему должно быть понятно, что
за объект и что внутри. `__str__` — для того, кто читает вывод программы.
Помните, что контейнер печатает элементы через `__repr__`.
"""


class Book:
    """Книга: название и год издания."""

    def __init__(self, title: str, year: int) -> None:
        """Сохранить название и год."""
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        """Отладочный вид: `Book('Мастер', 1967)`.

        Название в одинарных кавычках — так его печатает repr строки.
        """
        raise NotImplementedError("Implement me")

    def __str__(self) -> str:
        """Читаемый вид: `Мастер (1967)`."""
        raise NotImplementedError("Implement me")

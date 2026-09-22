"""Задача 5. Эмиттер событий.

Внутри класса — словарь «событие -> список обработчиков». Подписка,
рассылка, отписка. Связанный метод одного объекта — не метод другого,
и подписки это должны уважать. Последняя подзадача — со звёздочкой.
"""

from collections.abc import Callable
from typing import Any


class Emitter:
    """Рассылает события подписчикам."""

    def __init__(self) -> None:
        """Пустой словарь подписок."""
        raise NotImplementedError("Implement me")

    def on(self, event: str, handler: Callable[..., Any]) -> None:
        """Подписать обработчик на событие.

        Повторная подписка той же функции не дублирует запись.
        """
        raise NotImplementedError("Implement me")

    def emit(self, event: str, *args: Any) -> int:
        """Вызвать обработчиков события по порядку и вернуть их число.

        Аргументы события передаются каждому обработчику.
        Неизвестное событие — 0.
        """
        raise NotImplementedError("Implement me")

    def off(self, event: str, handler: Callable[..., Any]) -> bool:
        """Отписать обработчик.

        True — если подписка была, False — если такой подписки нет.
        """
        raise NotImplementedError("Implement me")

    def once(self, event: str, handler: Callable[..., Any]) -> None:
        """(*) Сработает один раз и снимет сам себя.

        Обёртка-посредник: при первом вызове сначала отписывается,
        затем зовёт handler. Вложенная функция — как в ДЗ apply,
        это разрешено.
        """
        raise NotImplementedError("Implement me")

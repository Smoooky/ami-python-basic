"""Задача 5. Эмиттер событий — решения."""

from collections.abc import Callable
from typing import Any


class Emitter:
    """Рассылает события подписчикам."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[..., Any]]] = {}

    def on(self, event: str, handler: Callable[..., Any]) -> None:
        handlers = self._handlers.setdefault(event, [])
        if handler not in handlers:  # повторная подписка не дублирует
            handlers.append(handler)

    def emit(self, event: str, *args: Any) -> int:
        # Снимок: обработчик (например, once) может отписаться прямо в цикле.
        snapshot = list(self._handlers.get(event, []))
        for handler in snapshot:
            handler(*args)
        return len(snapshot)

    def off(self, event: str, handler: Callable[..., Any]) -> bool:
        handlers = self._handlers.get(event)
        if handlers is not None and handler in handlers:
            handlers.remove(handler)
            return True
        return False

    def once(self, event: str, handler: Callable[..., Any]) -> None:
        def wrapper(*args: Any) -> None:
            self.off(event, wrapper)  # снять саму себя, затем позвать handler
            handler(*args)

        self.on(event, wrapper)

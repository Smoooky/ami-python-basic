from collections.abc import Generator, Iterable

# Команда кассе: число — цена блюда, строка — «пересчёт», «оплата» или «сбой».
Command = int | str


def session(log: list[str]) -> Generator[int, int | None, None]:
    raise NotImplementedError("Implement me")


def run(commands: Iterable[Command], log: list[str]) -> int:
    raise NotImplementedError("Implement me")


def totals(prices: Iterable[int], log: list[str]) -> Generator[int, None, None]:
    raise NotImplementedError("Implement me")

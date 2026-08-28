from collections.abc import Iterable, Iterator, Set


class Tags(Set[str]):
    def __init__(self, *names: str) -> None:
        raise NotImplementedError("Implement me")

    @staticmethod
    def normalize(name: str) -> str:
        raise NotImplementedError("Implement me")

    @classmethod
    def of(cls, names: Iterable[str]) -> Tags:
        raise NotImplementedError("Implement me")

    # В stdlib метод объявлен свободнее, чем нужно нам: он обещает вернуть
    # любое множество, а мы сужаем результат до Tags — отсюда type: ignore.
    @classmethod
    def _from_iterable(cls, iterable: Iterable[str]) -> Tags:  # type: ignore[override]
        raise NotImplementedError("Implement me")

    def __contains__(self, name: object) -> bool:
        raise NotImplementedError("Implement me")

    def __iter__(self) -> Iterator[str]:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __hash__(self) -> int:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")

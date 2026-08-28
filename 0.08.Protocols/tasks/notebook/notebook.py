import abc


class Notebook(abc.ABC):
    # Четыре абстрактных метода ниже уже объявлены — менять их не нужно.
    # Реализация каждого появляется только в потомках.

    @abc.abstractmethod
    def read(self, title: str) -> str:
        """Текст записи. Возбуждает KeyError, если такой записи нет."""

    @abc.abstractmethod
    def write(self, title: str, text: str) -> None:
        """Записывает текст, затирая старый."""

    @abc.abstractmethod
    def erase(self, title: str) -> None:
        """Стирает запись. Возбуждает KeyError, если такой записи нет."""

    @abc.abstractmethod
    def titles(self) -> list[str]:
        """Заголовки всех записей, отсортированные по возрастанию."""

    # А эти пять — писать вам, и только через четыре метода выше.

    def get(self, title: str, default: str | None = None) -> str | None:
        raise NotImplementedError("Implement me")

    def write_many(self, notes: dict[str, str]) -> None:
        raise NotImplementedError("Implement me")

    def copy_to(self, other: Notebook) -> int:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __contains__(self, title: str) -> bool:
        raise NotImplementedError("Implement me")


class PlainNotebook(Notebook):
    """Обычная тетрадь: записи лежат в словаре.

    Класс дан готовым — как образец реализации интерфейса. Менять его не нужно.
    """

    def __init__(self, notes: dict[str, str] | None = None) -> None:
        self._notes: dict[str, str] = {}
        if notes is not None:
            self.write_many(notes)

    def read(self, title: str) -> str:
        return self._notes[title]

    def write(self, title: str, text: str) -> None:
        self._notes[title] = text

    def erase(self, title: str) -> None:
        del self._notes[title]

    def titles(self) -> list[str]:
        return sorted(self._notes)


class Section(Notebook):
    def __init__(self, inner: Notebook, prefix: str) -> None:
        raise NotImplementedError("Implement me")

    def read(self, title: str) -> str:
        raise NotImplementedError("Implement me")

    def write(self, title: str, text: str) -> None:
        raise NotImplementedError("Implement me")

    def erase(self, title: str) -> None:
        raise NotImplementedError("Implement me")

    def titles(self) -> list[str]:
        raise NotImplementedError("Implement me")

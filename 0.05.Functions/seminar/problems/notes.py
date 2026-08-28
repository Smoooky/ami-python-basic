"""Задача 3. Класс, у которого состояние принадлежит объекту.

Списки и словари объекта создаются в `__init__`. Список, объявленный в теле
класса, был бы один на все записные книжки сразу — тесты это проверяют.
"""


class Notebook:
    """Записная книжка: заголовок и список записей."""

    def __init__(self, title: str) -> None:
        """Пустая книжка с заданным заголовком."""
        raise NotImplementedError("Implement me")

    def add(self, text: str) -> None:
        """Дописать запись в конец."""
        raise NotImplementedError("Implement me")

    def size(self) -> int:
        """Сколько записей в книжке."""
        raise NotImplementedError("Implement me")

    def latest(self) -> str:
        """Последняя запись. Если книжка пуста — пустая строка."""
        raise NotImplementedError("Implement me")

    def search(self, part: str) -> list[str]:
        """Записи, содержащие указанный кусок текста, в порядке добавления."""
        raise NotImplementedError("Implement me")

    def describe(self) -> str:
        """Строка вида "Дневник, записей: 3".

        Такой порядок слов согласуется с любым числом, в отличие от
        "3 записи".
        """
        raise NotImplementedError("Implement me")

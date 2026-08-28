"""Печатает документ вместе с указателем на каждое его значение.

На оценку не влияет и в проверке не участвует — это инструмент для вас.
Запуск: python demo.py
"""

from pointer import pointers, resolve

DOCUMENT: dict[str, object] = {
    "название": "Отчёт за сентябрь",
    "авторы": [
        {"имя": "Иванов", "теги": ["физика", "оптика"]},
        {"имя": "Петрова", "теги": []},
    ],
    "страниц": 12,
    "черновик": False,
    "правки": None,
    "": "значение под пустым ключом",
    "раздел/подраздел": "в ключе косая черта",
    "формула~1": "в ключе тильда",
}


def describe(value: object) -> str:
    if isinstance(value, dict):
        return f"объект, ключей: {len(value)}"
    if isinstance(value, list):
        return f"массив, элементов: {len(value)}"
    return repr(value)


def main() -> None:
    found = pointers(DOCUMENT)
    width = max(len(repr(pointer)) for pointer in found)
    print(f"{'указатель':<{width}}  значение")
    print("─" * (width + 2 + 40))
    for pointer in found:
        depth = pointer.count("/")
        shown = "  " * depth + describe(resolve(DOCUMENT, pointer))
        print(f"{pointer!r:<{width}}  {shown}")
    print()
    print(f"всего значений в документе: {len(found)}")


if __name__ == "__main__":
    main()

"""Показывает, чем разбор по запятой отличается от разбора по формату.

На оценку не влияет и в проверке не участвует — это инструмент для вас.
Запуск: python demo.py
"""

from fields import dump, parse

TABLE = [
    ["фамилия", "город", "заметка"],
    ["Иванов", "Москва, Россия", "переехал"],
    ["Петрова", "Казань", 'сказала "перезвоню"'],
    ["Сидоров", "Тверь", "первая строка\r\nвторая строка"],
]


def visible(text: str) -> str:
    """Помечает конец каждой строки знаком ⏎, чтобы его было видно."""
    return text.replace("\r\n", "\n").replace("\n", "⏎\n")


def show(text: str, indent: str = "        ") -> None:
    for line in visible(text).splitlines():
        print(indent + line)


def main() -> None:
    print("Исходная таблица:")
    for row in TABLE:
        print("       ", row)

    print("\nНаивно, через ','.join, и обратно через split(','):")
    for row in TABLE:
        naive = ",".join(row)
        back = naive.split(",")
        if back != row:
            verdict = f"полей было {len(row)}, после split стало {len(back)}"
        elif "\n" in naive:
            verdict = "одна запись растеклась на две строки файла"
        else:
            verdict = "совпало"
        print(f"    {verdict}")
        show(naive)

    text = dump(TABLE)
    print("\nПо формату, через dump:")
    show(text, indent="    ")

    restored = parse(text)
    print("\nОбратный разбор через parse:")
    for row in restored:
        print("       ", row)

    print()
    print(f"записей после разбора: {len(restored)}, было {len(TABLE)}")
    print(f"parse(dump(TABLE)) == TABLE: {restored == TABLE}")


if __name__ == "__main__":
    main()

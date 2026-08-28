"""Строит небольшое дерево во временном каталоге и показывает, что нашёл обход.

На оценку не влияет и в проверке не участвует — это инструмент для вас.
Запуск: python demo.py
"""

import tempfile
from pathlib import Path

from scan import by_suffix, first, largest, take, total_size, walk

LAYOUT = {
    "конспект.txt": "две строки\nвторая\n",
    "картинка.png": "0" * 120,
    "readme": "файл без расширения",
    "лекции/первая.txt": "а",
    "лекции/вторая.txt": "бб",
    "лекции/черновики/набросок.md": "# набросок",
    "пусто/.keep": "",
}


def build(root: Path) -> None:
    for name, text in LAYOUT.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as name:
        root = Path(name)
        build(root)

        print("что нашёл обход, в том порядке, в каком отдаёт:")
        for path in walk(root):
            print(f"  {str(path.relative_to(root)):<32}{path.stat().st_size:>6} б")

        biggest = largest(root)
        print()
        print(f"  расширения    {by_suffix(root)}")
        print(f"  всего байт    {total_size(root)}")
        print(f"  самый большой {biggest.name if biggest else 'файлов нет'}")
        found = first(root, ".md")
        print(f"  первый .md    {found.relative_to(root) if found else 'нет'}")

        print("\n  первые два файла — остальное дерево при этом не читается:")
        for path in take(walk(root), 2):
            print("   ", path.relative_to(root))


if __name__ == "__main__":
    main()

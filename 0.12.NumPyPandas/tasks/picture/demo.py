"""Наглядная проверка: рисует картинку, прогоняет её через ваши функции
и раскладывает результаты в PNG рядом с этим файлом.

    python demo.py

Тесты говорят «не сошлось», а картинки показывают, что именно не сошлось:
перепутанные оси зеркала или почерневшие вместо белых пиксели видно сразу.
На оценку demo.py не влияет — это инструмент для вас.
"""

import struct
import zlib
from pathlib import Path

import numpy as np
from picture import (
    Image,
    brighten,
    count_dark,
    crop,
    flip_left_right,
    flip_upside_down,
    invert,
    threshold,
)

HERE = Path(__file__).parent
HEIGHT, WIDTH = 120, 160


def write_png(path: Path, image: Image) -> None:
    """Сохранить массив в PNG. Ничего, кроме стандартной библиотеки."""
    rgb = np.dstack([image] * 3) if image.ndim == 2 else image
    raw = b"".join(b"\x00" + row.tobytes() for row in rgb.astype(np.uint8))

    def chunk(tag: bytes, data: bytes) -> bytes:
        body = tag + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    header = struct.pack(">IIBBBBB", rgb.shape[1], rgb.shape[0], 8, 2, 0, 0, 0)
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", header)
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )


def source() -> Image:
    """Фон-градиент, белая буква «F» и очень светлый квадрат в углу."""
    image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)
    image[:] = np.linspace(20, 200, WIDTH, dtype=np.uint8)

    # Буква «F»: несимметрична и по горизонтали, и по вертикали, поэтому
    # по ней сразу видно, какое именно зеркало получилось.
    image[20:100, 30:42] = 255
    image[20:32, 30:100] = 255
    image[52:64, 30:80] = 255

    # Квадрат почти предельной яркости: при неверном brighten он почернеет.
    image[8:20, 130:150] = 250
    return image


def main() -> None:
    image = source()
    results: dict[str, Image] = {
        "source": image,
        "crop": crop(image, 20, 30, 80, 70),
        "flip-left-right": flip_left_right(image),
        "flip-upside-down": flip_upside_down(image),
        "invert": invert(image),
        "brighten": brighten(image, 60),
        "darken": brighten(image, -60),
        "threshold": threshold(image, 128),
    }
    for name, result in results.items():
        write_png(HERE / f"demo-{name}.png", result)
        print(f"demo-{name}.png  {result.shape[1]}x{result.shape[0]}")

    print(f"\nтёмных пикселей (ярче 0, темнее 128): {count_dark(image, 128)}")
    print("Откройте demo-*.png: буква «F» должна отразиться в нужную сторону,")
    print("а светлый квадрат на demo-brighten.png остаться светлым, а не почернеть.")


if __name__ == "__main__":
    main()

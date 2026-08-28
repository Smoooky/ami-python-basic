"""Наглядная проверка: рисует цветную картинку, прогоняет её через ваши
функции и раскладывает результаты в PNG рядом с этим файлом.

    python demo.py

Каналы, зеркало и склейки удобнее проверять глазами: перепутанные оси или
каналы видно сразу, а тест про это скажет только «формы не совпали».
На оценку demo.py не влияет — это инструмент для вас.
"""

import struct
import zlib
from pathlib import Path

import numpy as np
from palette import (
    BLUE,
    GREEN,
    RED,
    Colour,
    Gray,
    channel,
    from_channels,
    side_by_side,
    stacked,
    swap_red_and_blue,
    to_gray,
)

HERE = Path(__file__).parent
HEIGHT, WIDTH = 120, 160


def write_png(path: Path, image: Colour | Gray) -> None:
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


def source() -> Colour:
    """Три чистых квадрата, синий фон-градиент и жёлтая буква «F»."""
    image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    image[..., BLUE] = np.linspace(30, 160, WIDTH, dtype=np.uint8)

    # Чистые красный, зелёный и синий: после to_gray они станут заметно
    # разными оттенками серого — 76, 150 и 29.
    image[8:32, 8:48] = (255, 0, 0)
    image[8:32, 56:96] = (0, 255, 0)
    image[8:32, 104:144] = (0, 0, 255)

    # Жёлтая «F»: несимметрична, поэтому зеркало ни с чем не спутаешь.
    image[45:110, 25:37] = (255, 230, 0)
    image[45:57, 25:95] = (255, 230, 0)
    image[72:84, 25:75] = (255, 230, 0)
    return image


def main() -> None:
    image = source()
    half = image[:, : WIDTH // 2]

    results: dict[str, Colour | Gray] = {
        "source": image,
        "channel-red": channel(image, RED),
        "channel-green": channel(image, GREEN),
        "channel-blue": channel(image, BLUE),
        "swapped": swap_red_and_blue(image),
        "gray": to_gray(image),
        "side-by-side": side_by_side(half, swap_red_and_blue(half)),
        "stacked": stacked(half, swap_red_and_blue(half)),
        "rebuilt": from_channels(channel(image, RED), channel(image, GREEN), channel(image, BLUE)),
    }
    for name, result in results.items():
        write_png(HERE / f"demo-{name}.png", result)
        print(f"demo-{name}.png  {result.shape[1]}x{result.shape[0]}")

    print("\nЧто смотреть:")
    print("  demo-channel-*.png — квадрат своего цвета белый, два других чёрные;")
    print("  demo-swapped.png   — красный квадрат стал синим, зелёный не изменился;")
    print("  demo-gray.png      — зелёный квадрат светлее красного, синий темнее всех;")
    print("  demo-side-by-side  — шире исходника, demo-stacked — выше;")
    print("  demo-rebuilt.png   — обязан совпасть с demo-source.png.")


if __name__ == "__main__":
    main()

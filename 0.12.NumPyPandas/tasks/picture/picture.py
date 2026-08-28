import numpy as np
import numpy.typing as npt

# Чёрно-белое изображение: двумерная таблица яркостей от 0 до 255.
Image = npt.NDArray[np.uint8]


def check(image: Image) -> None:
    raise NotImplementedError("Implement me")


def crop(image: Image, top: int, left: int, height: int, width: int) -> Image:
    raise NotImplementedError("Implement me")


def flip_left_right(image: Image) -> Image:
    raise NotImplementedError("Implement me")


def flip_upside_down(image: Image) -> Image:
    raise NotImplementedError("Implement me")


def invert(image: Image) -> Image:
    raise NotImplementedError("Implement me")


def brighten(image: Image, amount: int) -> Image:
    raise NotImplementedError("Implement me")


def threshold(image: Image, level: int) -> Image:
    raise NotImplementedError("Implement me")


def count_dark(image: Image, level: int) -> int:
    raise NotImplementedError("Implement me")

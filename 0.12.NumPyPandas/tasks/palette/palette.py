import numpy as np
import numpy.typing as npt

# Цветная картинка: (высота, ширина, 3) — красный, зелёный и синий канал.
Colour = npt.NDArray[np.uint8]
# Одноканальная картинка: (высота, ширина).
Gray = npt.NDArray[np.uint8]

RED, GREEN, BLUE = 0, 1, 2

# Веса, с которыми глаз видит каналы: зелёный он различает лучше всего.
LUMA = np.array([0.299, 0.587, 0.114])


def check(image: Colour) -> None:
    raise NotImplementedError("Implement me")


def check_gray(image: Gray) -> None:
    raise NotImplementedError("Implement me")


def channel(image: Colour, number: int) -> Gray:
    raise NotImplementedError("Implement me")


def swap_red_and_blue(image: Colour) -> Colour:
    raise NotImplementedError("Implement me")


def from_channels(red: Gray, green: Gray, blue: Gray) -> Colour:
    raise NotImplementedError("Implement me")


def to_gray(image: Colour) -> Gray:
    raise NotImplementedError("Implement me")


def side_by_side(left: Colour, right: Colour) -> Colour:
    raise NotImplementedError("Implement me")


def stacked(top: Colour, bottom: Colour) -> Colour:
    raise NotImplementedError("Implement me")

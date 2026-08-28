import numpy as np
import pytest
from palette import (
    BLUE,
    GREEN,
    RED,
    Colour,
    channel,
    from_channels,
    side_by_side,
    stacked,
    swap_red_and_blue,
    to_gray,
)


def flag() -> Colour:
    """Четыре пикселя: красный, зелёный, синий и белый."""
    return np.array(
        [
            [[255, 0, 0], [0, 255, 0]],
            [[0, 0, 255], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )


def test_channel() -> None:
    image = flag()
    assert channel(image, RED).tolist() == [[255, 0], [0, 255]]
    assert channel(image, GREEN).tolist() == [[0, 255], [0, 255]]
    assert channel(image, BLUE).tolist() == [[0, 0], [255, 255]]
    assert channel(image, RED).shape == (2, 2)


def test_channel_is_a_view() -> None:
    image = flag()
    red = channel(image, RED)
    red[0, 0] = 7
    assert image[0, 0, RED] == 7


def test_channel_number_is_checked() -> None:
    with pytest.raises(ValueError):
        channel(flag(), 3)
    with pytest.raises(ValueError):
        channel(flag(), -1)


def test_swap_red_and_blue() -> None:
    image = flag()
    result = swap_red_and_blue(image)
    assert result[0, 0].tolist() == [0, 0, 255]
    assert result[1, 0].tolist() == [255, 0, 0]
    assert np.array_equal(swap_red_and_blue(result), image)


def test_from_channels() -> None:
    red = np.array([[10, 20]], dtype=np.uint8)
    green = np.array([[30, 40]], dtype=np.uint8)
    blue = np.array([[50, 60]], dtype=np.uint8)

    image = from_channels(red, green, blue)
    assert image.shape == (1, 2, 3)
    assert image[0, 0].tolist() == [10, 30, 50]
    assert image.dtype == np.uint8


def test_from_channels_and_channel_are_opposites() -> None:
    image = flag()
    parts = [channel(image, number) for number in (RED, GREEN, BLUE)]
    assert np.array_equal(from_channels(*parts), image)


def test_to_gray() -> None:
    result = to_gray(flag())
    assert result.shape == (2, 2)
    assert result.dtype == np.uint8
    # 0.299, 0.587 и 0.114 от 255 — зелёный кажется самым светлым
    assert result.tolist() == [[76, 150], [29, 255]]


def test_side_by_side_and_stacked() -> None:
    image = flag()
    assert side_by_side(image, image).shape == (2, 4, 3)
    assert stacked(image, image).shape == (4, 2, 3)
    assert np.array_equal(side_by_side(image, image)[:, :2], image)
    assert np.array_equal(stacked(image, image)[:2], image)


def test_glueing_checks_the_sizes() -> None:
    tall = np.zeros((3, 2, 3), dtype=np.uint8)
    wide = np.zeros((2, 5, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        side_by_side(flag(), tall)
    with pytest.raises(ValueError):
        stacked(flag(), wide)


def test_shape_and_dtype_are_checked() -> None:
    with pytest.raises(ValueError):
        channel(np.zeros((2, 2), dtype=np.uint8), RED)
    with pytest.raises(ValueError):
        to_gray(np.zeros((2, 2, 4), dtype=np.uint8))
    with pytest.raises(ValueError):
        to_gray(np.zeros((2, 2, 3), dtype=np.int16))

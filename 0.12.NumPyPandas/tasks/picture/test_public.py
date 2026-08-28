import numpy as np
import pytest
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


def sample() -> Image:
    return np.array(
        [
            [0, 10, 20, 30],
            [40, 50, 60, 70],
            [80, 90, 100, 110],
        ],
        dtype=np.uint8,
    )


def test_crop() -> None:
    piece = crop(sample(), 1, 1, 2, 2)
    assert np.array_equal(piece, np.array([[50, 60], [90, 100]], dtype=np.uint8))
    assert piece.shape == (2, 2)


def test_crop_is_a_view() -> None:
    image = sample()
    piece = crop(image, 0, 0, 2, 2)
    assert np.shares_memory(piece, image)
    piece[0, 0] = 255
    assert image[0, 0] == 255


def test_crop_checks_the_rectangle() -> None:
    image = sample()
    with pytest.raises(ValueError):
        crop(image, 0, 0, 0, 2)
    with pytest.raises(ValueError):
        crop(image, 2, 0, 2, 2)
    with pytest.raises(ValueError):
        crop(image, -1, 0, 1, 1)


def test_flips() -> None:
    image = sample()
    assert np.array_equal(flip_left_right(image)[0], [30, 20, 10, 0])
    assert np.array_equal(flip_upside_down(image)[0], [80, 90, 100, 110])
    assert np.array_equal(flip_left_right(flip_left_right(image)), image)


def test_invert() -> None:
    result = invert(sample())
    assert result.dtype == np.uint8
    assert np.array_equal(result[0], [255, 245, 235, 225])
    assert np.array_equal(invert(invert(sample())), sample())


def test_brighten() -> None:
    result = brighten(sample(), 30)
    assert result.dtype == np.uint8
    assert np.array_equal(result[0], [30, 40, 50, 60])


def test_brighten_does_not_wrap_around() -> None:
    image = np.array([[200, 250]], dtype=np.uint8)
    assert np.array_equal(brighten(image, 100), [[255, 255]])
    assert np.array_equal(brighten(image, -250), [[0, 0]])


def test_threshold_and_count_dark() -> None:
    result = threshold(sample(), 50)
    assert result.dtype == np.uint8
    assert np.array_equal(result[0], [0, 0, 0, 0])
    assert np.array_equal(result[1], [0, 0, 255, 255])
    assert count_dark(sample(), 50) == 5
    assert count_dark(sample(), 0) == 0

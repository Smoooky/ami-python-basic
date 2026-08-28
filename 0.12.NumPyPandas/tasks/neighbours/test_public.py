import numpy as np
import pytest
from neighbours import Points, closest_pair, distances, farthest_from_all, nearest, within

DORMS: Points = np.array([[0.0, 0.0], [10.0, 0.0], [0.0, 10.0]])
CAFES: Points = np.array([[1.0, 0.0], [9.0, 1.0], [5.0, 5.0]])


def test_distances_shape_and_values() -> None:
    matrix = distances(DORMS, CAFES)
    assert matrix.shape == (3, 3)
    assert np.isclose(matrix[0, 0], 1.0)
    assert np.isclose(matrix[1, 1], np.sqrt(2))
    assert np.isclose(matrix[2, 2], np.sqrt(50))


def test_distance_to_itself_is_zero() -> None:
    matrix = distances(DORMS, DORMS)
    assert np.allclose(np.diag(matrix), 0.0)
    assert np.allclose(matrix, matrix.T)


def test_nearest() -> None:
    result = nearest(DORMS, CAFES)
    assert result.tolist() == [0, 1, 2]
    assert result.shape == (3,)


def test_within() -> None:
    mask = within(DORMS, CAFES, 2.0)
    assert mask.dtype == np.bool_
    assert mask.shape == (3, 3)
    assert mask[0].tolist() == [True, False, False]
    assert within(DORMS, CAFES, 100.0).all()
    assert not within(DORMS, CAFES, 0.5).any()


def test_closest_pair() -> None:
    points = np.array([[0.0, 0.0], [100.0, 0.0], [1.0, 0.0]])
    assert closest_pair(points) == (0, 2)


def test_farthest_from_all() -> None:
    # Третьему общежитию до ближайшей кофейни дальше всех.
    assert farthest_from_all(DORMS, CAFES) == 2


def test_arguments_are_checked() -> None:
    with pytest.raises(ValueError):
        distances(np.array([1.0, 2.0]), CAFES)
    with pytest.raises(ValueError):
        distances(np.zeros((0, 2)), CAFES)
    with pytest.raises(ValueError):
        distances(DORMS, np.zeros((2, 3)))
    with pytest.raises(ValueError):
        within(DORMS, CAFES, -1.0)
    with pytest.raises(ValueError):
        closest_pair(np.array([[0.0, 0.0]]))

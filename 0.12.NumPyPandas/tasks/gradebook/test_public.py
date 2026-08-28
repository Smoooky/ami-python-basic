import numpy as np
import pytest
from gradebook import (
    Table,
    best_student,
    centred,
    hardest_task,
    passed,
    scaled,
    student_means,
    task_means,
)


def journal() -> Table:
    # три студента, четыре работы
    return np.array(
        [
            [10.0, 20.0, 30.0, 40.0],
            [40.0, 30.0, 20.0, 10.0],
            [50.0, 50.0, 50.0, 50.0],
        ]
    )


def test_means() -> None:
    assert np.allclose(student_means(journal()), [25.0, 25.0, 50.0])
    assert np.allclose(task_means(journal()), [100 / 3, 100 / 3, 100 / 3, 100 / 3])
    assert student_means(journal()).shape == (3,)
    assert task_means(journal()).shape == (4,)


def test_centred() -> None:
    result = centred(journal())
    assert result.shape == journal().shape
    assert np.allclose(result[0], [-15.0, -5.0, 5.0, 15.0])
    assert np.allclose(result.mean(axis=1), 0.0)


def test_scaled() -> None:
    result = scaled(journal())
    assert result.shape == journal().shape
    assert np.allclose(result.max(axis=0), 100.0)
    assert np.allclose(result[:, 0], [20.0, 80.0, 100.0])


def test_scaled_survives_a_task_nobody_solved() -> None:
    table = np.array([[0.0, 5.0], [0.0, 10.0]])
    result = scaled(table)
    assert np.allclose(result[:, 0], [0.0, 0.0])
    assert np.allclose(result[:, 1], [50.0, 100.0])


def test_best_student_and_hardest_task() -> None:
    assert best_student(journal()) == 2
    assert isinstance(best_student(journal()), int)

    table = np.array([[10.0, 1.0], [10.0, 3.0]])
    assert hardest_task(table) == 1


def test_passed() -> None:
    result = passed(journal(), 20.0)
    assert result.dtype == np.bool_
    assert result.tolist() == [False, False, True]
    assert passed(journal(), 0.0).tolist() == [True, True, True]


def test_empty_and_wrong_shape() -> None:
    with pytest.raises(ValueError):
        student_means(np.array([]))
    with pytest.raises(ValueError):
        task_means(np.array([1.0, 2.0]))

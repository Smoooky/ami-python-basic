import numpy as np
import numpy.typing as npt

# Набор точек: строка — точка, столбцы — её координаты.
Points = npt.NDArray[np.float64]


def check(points: Points, others: Points | None = None) -> None:
    raise NotImplementedError("Implement me")


def distances(points: Points, others: Points) -> npt.NDArray[np.float64]:
    raise NotImplementedError("Implement me")


def nearest(points: Points, others: Points) -> npt.NDArray[np.intp]:
    raise NotImplementedError("Implement me")


def within(points: Points, others: Points, radius: float) -> npt.NDArray[np.bool_]:
    raise NotImplementedError("Implement me")


def closest_pair(points: Points) -> tuple[int, int]:
    raise NotImplementedError("Implement me")


def farthest_from_all(points: Points, others: Points) -> int:
    raise NotImplementedError("Implement me")

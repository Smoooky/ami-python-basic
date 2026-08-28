import numpy as np
import numpy.typing as npt

# Журнал: строки — студенты, столбцы — работы, значения — баллы.
Table = npt.NDArray[np.float64]


def check(table: Table) -> None:
    raise NotImplementedError("Implement me")


def student_means(table: Table) -> npt.NDArray[np.float64]:
    raise NotImplementedError("Implement me")


def task_means(table: Table) -> npt.NDArray[np.float64]:
    raise NotImplementedError("Implement me")


def centred(table: Table) -> Table:
    raise NotImplementedError("Implement me")


def scaled(table: Table) -> Table:
    raise NotImplementedError("Implement me")


def best_student(table: Table) -> int:
    raise NotImplementedError("Implement me")


def hardest_task(table: Table) -> int:
    raise NotImplementedError("Implement me")


def passed(table: Table, threshold: float) -> npt.NDArray[np.bool_]:
    raise NotImplementedError("Implement me")

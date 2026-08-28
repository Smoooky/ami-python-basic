import numpy as np
import numpy.typing as npt

# Поле: True — живая клетка, False — мёртвая.
Board = npt.NDArray[np.bool_]

ALIVE = "#"
DEAD = "."


def check(board: Board) -> None:
    raise NotImplementedError("Implement me")


def from_text(lines: list[str]) -> Board:
    raise NotImplementedError("Implement me")


def to_text(board: Board) -> list[str]:
    raise NotImplementedError("Implement me")


def neighbours(board: Board) -> npt.NDArray[np.int8]:
    raise NotImplementedError("Implement me")


def step(board: Board) -> Board:
    raise NotImplementedError("Implement me")


def run(board: Board, steps: int) -> Board:
    raise NotImplementedError("Implement me")

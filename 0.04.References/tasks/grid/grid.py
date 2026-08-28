Matrix = list[list[int]]


def make(rows: int, cols: int, fill: int = 0) -> Matrix:
    raise NotImplementedError("Implement me")


def is_rectangular(matrix: Matrix) -> bool:
    raise NotImplementedError("Implement me")


def set_cell(matrix: Matrix, row: int, col: int, value: int) -> None:
    raise NotImplementedError("Implement me")


def row_sums(matrix: Matrix) -> list[int]:
    raise NotImplementedError("Implement me")


def column_sums(matrix: Matrix) -> list[int]:
    raise NotImplementedError("Implement me")


def transpose(matrix: Matrix) -> Matrix:
    raise NotImplementedError("Implement me")

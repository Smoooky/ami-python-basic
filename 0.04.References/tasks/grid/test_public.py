from grid import Matrix, column_sums, is_rectangular, make, row_sums, set_cell, transpose


def test_make() -> None:
    assert make(2, 3) == [[0, 0, 0], [0, 0, 0]]
    assert make(2, 2, 7) == [[7, 7], [7, 7]]
    assert make(0, 5) == []


def test_rows_are_separate_objects() -> None:
    matrix = make(3, 3)
    set_cell(matrix, 0, 0, 5)

    assert matrix[0] == [5, 0, 0]
    assert matrix[1] == [0, 0, 0]
    assert matrix[2] == [0, 0, 0]
    assert matrix[0] is not matrix[1]


def test_set_cell_changes_in_place() -> None:
    matrix = make(2, 2)
    same = matrix
    set_cell(matrix, 1, 1, 9)
    assert same[1][1] == 9


def test_is_rectangular() -> None:
    assert is_rectangular([[1, 2], [3, 4]]) is True
    assert is_rectangular([[1, 2], [3]]) is False
    assert is_rectangular([]) is False
    assert is_rectangular([[]]) is False


def test_sums() -> None:
    matrix: Matrix = [[1, 2, 3], [4, 5, 6]]
    assert row_sums(matrix) == [6, 15]
    assert column_sums(matrix) == [5, 7, 9]


def test_transpose() -> None:
    matrix: Matrix = [[1, 2, 3], [4, 5, 6]]
    assert transpose(matrix) == [[1, 4], [2, 5], [3, 6]]
    assert transpose(transpose(matrix)) == matrix


def test_transpose_makes_a_new_matrix() -> None:
    matrix: Matrix = [[1, 2], [3, 4]]
    result = transpose(matrix)
    result[0][0] = 99
    assert matrix[0][0] == 1

from grids import distinct_rows, make_grid, set_cell, shares_rows


def test_make_grid_shape() -> None:
    assert make_grid(2, 3) == [[0, 0, 0], [0, 0, 0]]
    assert make_grid(1, 1) == [[0]]
    assert make_grid(0, 5) == []


def test_make_grid_rows_are_separate_objects() -> None:
    grid = make_grid(3, 3)
    assert grid[0] is not grid[1]
    assert grid[1] is not grid[2]


def test_make_grid_change_stays_in_one_row() -> None:
    grid = make_grid(3, 3)
    grid[0][0] = 1
    assert grid == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_set_cell() -> None:
    grid = make_grid(2, 2)
    set_cell(grid, 1, 0, 7)
    assert grid == [[0, 0], [7, 0]]


def test_set_cell_touches_only_one_row() -> None:
    grid = make_grid(3, 3)
    set_cell(grid, 1, 1, 9)
    assert grid == [[0, 0, 0], [0, 9, 0], [0, 0, 0]]


def test_set_cell_changes_the_same_object() -> None:
    grid = make_grid(2, 2)
    alias = grid
    set_cell(grid, 0, 1, 5)
    assert alias[0][1] == 5


def test_distinct_rows() -> None:
    assert distinct_rows(make_grid(3, 3)) == 3
    assert distinct_rows([]) == 0


def test_distinct_rows_counts_objects_not_values() -> None:
    row = [0, 0]
    assert distinct_rows([row, row, [0, 0]]) == 2
    assert distinct_rows([[0, 0], [0, 0]]) == 2


def test_shares_rows() -> None:
    row = [1, 2]
    assert shares_rows([row, row]) is True
    assert shares_rows([[1, 2], [1, 2]]) is False
    assert shares_rows(make_grid(4, 4)) is False


def test_shares_rows_on_short_grids() -> None:
    assert shares_rows([]) is False
    assert shares_rows([[1]]) is False

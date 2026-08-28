from render_table import render_table


def test_two_columns() -> None:
    rows = [["имя", "балл"], ["Алиса", "10"], ["Боб", "9"]]
    assert render_table(rows, "<>") == [
        "имя   | балл",
        "------+-----",
        "Алиса |   10",
        "Боб   |    9",
    ]


def test_single_cell() -> None:
    assert render_table([["a"]], "<") == ["a", "-"]


def test_empty_table() -> None:
    assert render_table([], "<") == []

from dispatch import apply_all, apply_op, build_table, known


def test_build_table_has_four_operations() -> None:
    table = build_table()
    assert sorted(table) == ["максимум", "минус", "плюс", "умножить"]


def test_build_table_values_are_callable() -> None:
    table = build_table()
    assert table["плюс"](2, 3) == 5
    assert table["минус"](2, 3) == -1
    assert table["умножить"](2, 3) == 6
    assert table["максимум"](2, 3) == 3


def test_known() -> None:
    assert known(build_table()) == ["максимум", "минус", "плюс", "умножить"]
    assert known({}) == []


def test_apply_op() -> None:
    table = build_table()
    assert apply_op(table, "плюс", 2, 3) == 5
    assert apply_op(table, "максимум", -2, -3) == -2


def test_apply_op_with_an_unknown_name() -> None:
    assert apply_op(build_table(), "делить", 6, 3) is None
    assert apply_op({}, "плюс", 1, 1) is None


def test_apply_all() -> None:
    table = build_table()
    assert apply_all(table, ["плюс", "минус"], 10, 4) == [14, 6]
    assert apply_all(table, [], 1, 2) == []


def test_apply_all_keeps_unknown_names_as_none() -> None:
    table = build_table()
    assert apply_all(table, ["плюс", "делить", "минус"], 10, 4) == [14, None, 6]


def test_table_can_be_extended_without_touching_the_functions() -> None:
    table = build_table()
    table["удвоить"] = lambda a, b: (a + b) * 2
    assert apply_op(table, "удвоить", 1, 2) == 6
    assert "удвоить" in known(table)

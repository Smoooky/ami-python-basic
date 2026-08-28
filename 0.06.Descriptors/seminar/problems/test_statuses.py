from statuses import Status, is_final, parse, parse_all, values


def test_parse_known() -> None:
    assert parse("new") is Status.NEW
    assert parse("done") is Status.DONE


def test_parse_unknown() -> None:
    assert parse("что-то") is None
    assert parse("") is None


def test_parse_is_case_sensitive() -> None:
    # Значения объявлены строчными буквами, других вариантов нет.
    assert parse("NEW") is None


def test_parse_all() -> None:
    assert parse_all(["new", "paid"]) == [Status.NEW, Status.PAID]
    assert parse_all([]) == []


def test_parse_all_drops_unknown() -> None:
    assert parse_all(["new", "мусор", "done"]) == [Status.NEW, Status.DONE]


def test_values_keep_declaration_order() -> None:
    assert values() == ["new", "paid", "shipped", "done"]


def test_is_final() -> None:
    assert is_final(Status.DONE) is True
    assert is_final(Status.SHIPPED) is True
    assert is_final(Status.NEW) is False
    assert is_final(Status.PAID) is False

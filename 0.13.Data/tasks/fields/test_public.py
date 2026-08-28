import pytest
from fields import dump, join_row, needs_quotes, parse, quote, unquote


def test_needs_quotes() -> None:
    assert needs_quotes("Иванов") is False
    assert needs_quotes("") is False
    assert needs_quotes("Москва, Россия") is True
    assert needs_quotes('он сказал "да"') is True
    assert needs_quotes("две\r\nстроки") is True
    assert needs_quotes("одна\nстрока") is True


def test_quote() -> None:
    assert quote("Иванов") == "Иванов"
    assert quote("Москва, Россия") == '"Москва, Россия"'
    assert quote('он сказал "да"') == '"он сказал ""да"""'
    assert quote("") == ""


def test_unquote() -> None:
    assert unquote("Иванов") == "Иванов"
    assert unquote('"Москва, Россия"') == "Москва, Россия"
    assert unquote('"он сказал ""да"""') == 'он сказал "да"'
    assert unquote('""') == ""


def test_quote_and_unquote_are_inverse() -> None:
    for field in ["", "Иванов", "a,b", 'a"b', "a\r\nb", '"', ",,,", '""']:
        assert unquote(quote(field)) == field


def test_unquote_rejects_broken_fields() -> None:
    with pytest.raises(ValueError):
        unquote('"не закрыто')
    with pytest.raises(ValueError):
        unquote('"a"b"')
    with pytest.raises(ValueError):
        unquote('без кавычек, но с "')


def test_split_by_comma_would_be_wrong() -> None:
    line = 'Иванов,"Москва, Россия",78'
    assert line.split(",") == ["Иванов", '"Москва', ' Россия"', "78"]
    assert parse(line) == [["Иванов", "Москва, Россия", "78"]]


def test_parse_one_row() -> None:
    assert parse("a,b,c") == [["a", "b", "c"]]
    assert parse("a,,c") == [["a", "", "c"]]
    assert parse("") == []


def test_parse_many_rows() -> None:
    assert parse("a,b\r\nc,d\r\n") == [["a", "b"], ["c", "d"]]
    assert parse("a,b\nc,d") == [["a", "b"], ["c", "d"]]


def test_parse_keeps_newline_inside_quotes() -> None:
    assert parse('"две\r\nстроки",b\r\n') == [["две\r\nстроки", "b"]]


def test_parse_rejects_broken_text() -> None:
    with pytest.raises(ValueError):
        parse('"не закрыто')
    with pytest.raises(ValueError):
        parse('a"b')
    with pytest.raises(ValueError):
        parse('"a"мусор')


def test_join_row() -> None:
    assert join_row(["a", "b"]) == "a,b"
    assert join_row(["Иванов", "Москва, Россия"]) == 'Иванов,"Москва, Россия"'
    with pytest.raises(ValueError):
        join_row([])


def test_dump() -> None:
    assert dump([["a", "b"], ["c", "d"]]) == "a,b\r\nc,d\r\n"
    assert dump([]) == ""
    with pytest.raises(ValueError):
        dump([["a", "b"], ["c"]])


def test_dump_and_parse_are_inverse() -> None:
    tables = [
        [["a"]],
        [["Иванов", "Москва, Россия", "78"]],
        [["заголовок"], ['со "звёздочкой"'], ["две\r\nстроки"]],
        [[""]],
        [],
    ]
    for rows in tables:
        assert parse(dump(rows)) == rows

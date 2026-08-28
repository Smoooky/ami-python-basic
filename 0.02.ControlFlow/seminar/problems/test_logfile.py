from pathlib import Path

from logfile import count_lines, head_and_body, longest_line, write_lines


def make(tmp_path: Path, text: str) -> str:
    path = tmp_path / "data.txt"
    path.write_text(text, encoding="utf-8")
    return str(path)


def test_count_lines(tmp_path: Path) -> None:
    assert count_lines(make(tmp_path, "раз\nдва\nтри\n")) == 3
    assert count_lines(make(tmp_path, "")) == 0


def test_count_lines_without_a_trailing_newline(tmp_path: Path) -> None:
    assert count_lines(make(tmp_path, "раз\nдва")) == 2


def test_count_lines_counts_empty_lines(tmp_path: Path) -> None:
    assert count_lines(make(tmp_path, "\n\n\n")) == 3


def test_longest_line(tmp_path: Path) -> None:
    assert longest_line(make(tmp_path, "раз\nдлиннее\nдва\n")) == "длиннее"
    assert longest_line(make(tmp_path, "")) == ""


def test_longest_line_prefers_the_earlier_one(tmp_path: Path) -> None:
    assert longest_line(make(tmp_path, "раз\nдва\n")) == "раз"


def test_longest_line_keeps_leading_spaces(tmp_path: Path) -> None:
    # Убирается только перевод строки, отступ — часть данных.
    assert longest_line(make(tmp_path, "  отступ\nбез\n")) == "  отступ"


def test_head_and_body(tmp_path: Path) -> None:
    path = make(tmp_path, "первая\nвторая\n")
    assert head_and_body(path) == ("первая", "первая\nвторая\n")


def test_head_and_body_on_one_line(tmp_path: Path) -> None:
    path = make(tmp_path, "одна строка")
    assert head_and_body(path) == ("одна строка", "одна строка")


def test_head_and_body_on_an_empty_file(tmp_path: Path) -> None:
    assert head_and_body(make(tmp_path, "")) == ("", "")


def test_write_lines(tmp_path: Path) -> None:
    path = str(tmp_path / "out.txt")
    write_lines(path, ["раз", "два"])
    assert Path(path).read_text(encoding="utf-8") == "раз\nдва\n"


def test_write_lines_replaces_the_old_content(tmp_path: Path) -> None:
    path = make(tmp_path, "старое содержимое\n")
    write_lines(path, ["новое"])
    assert Path(path).read_text(encoding="utf-8") == "новое\n"


def test_write_lines_with_nothing_to_write(tmp_path: Path) -> None:
    path = make(tmp_path, "старое\n")
    write_lines(path, [])
    assert Path(path).read_text(encoding="utf-8") == ""


def test_write_and_count_agree(tmp_path: Path) -> None:
    path = str(tmp_path / "out.txt")
    write_lines(path, ["раз", "два", "три"])
    assert count_lines(path) == 3

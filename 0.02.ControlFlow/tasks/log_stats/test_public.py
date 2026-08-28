from pathlib import Path

from log_stats import log_stats


def test_sample(tmp_path: Path) -> None:
    path = tmp_path / "app.log"
    path.write_text(
        "INFO server started\nWARN disk usage 91%\nERROR cannot open file\nINFO request handled\n",
        encoding="utf-8",
    )
    assert log_stats(str(path)) == (4, 1, 1, 2)


def test_empty_file(tmp_path: Path) -> None:
    path = tmp_path / "empty.log"
    path.write_text("", encoding="utf-8")
    assert log_stats(str(path)) == (0, 0, 0, 0)


def test_blank_lines_are_ignored(tmp_path: Path) -> None:
    path = tmp_path / "blank.log"
    path.write_text("INFO a\n\n   \nINFO b\n", encoding="utf-8")
    assert log_stats(str(path)) == (2, 0, 0, 2)

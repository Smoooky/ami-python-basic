import types
from collections.abc import Iterator
from pathlib import Path

import pytest
from scan import by_suffix, first, largest, take, total_size, walk


@pytest.fixture
def tree(tmp_path: Path) -> Path:
    (tmp_path / "б.txt").write_text("бб\n", encoding="utf-8")
    (tmp_path / "а.txt").write_text("а\n", encoding="utf-8")
    (tmp_path / "картинка.png").write_bytes(b"0" * 40)
    (tmp_path / "readme").write_text("без расширения", encoding="utf-8")
    nested = tmp_path / "вложенный"
    nested.mkdir()
    (nested / "глубокий.txt").write_text("ггг\n", encoding="utf-8")
    return tmp_path


def names(paths: Iterator[Path] | list[Path], root: Path) -> list[str]:
    return [str(path.relative_to(root)) for path in paths]


def test_walk_finds_every_file(tree: Path) -> None:
    assert names(walk(tree), tree) == [
        "readme",
        "а.txt",
        "б.txt",
        "вложенный/глубокий.txt",
        "картинка.png",
    ]


def test_walk_yields_no_directories(tree: Path) -> None:
    for path in walk(tree):
        assert path.is_file()


def test_walk_is_a_generator(tree: Path) -> None:
    assert isinstance(walk(tree), types.GeneratorType)


def test_walk_does_nothing_until_asked(tmp_path: Path) -> None:
    # Тело генератора не запускается, пока у него не попросили значение.
    steps = walk(tmp_path / "такого-каталога-нет")
    with pytest.raises(FileNotFoundError):
        next(steps)


def test_take(tree: Path) -> None:
    assert names(take(walk(tree), 2), tree) == ["readme", "а.txt"]
    assert take(walk(tree), 0) == []
    assert len(take(walk(tree), 100)) == 5
    with pytest.raises(ValueError):
        take(walk(tree), -1)


def test_take_does_not_read_more_than_asked() -> None:
    def exploding(limit: int) -> Iterator[int]:
        yield from range(limit)
        raise AssertionError("итератор прочитали дальше нужного")

    assert take(exploding(3), 3) == [0, 1, 2]


def test_first(tree: Path) -> None:
    found = first(tree, ".png")
    assert found is not None and found.name == "картинка.png"
    assert first(tree, ".zip") is None
    empty = first(tree, "")
    assert empty is not None and empty.name == "readme"


def test_by_suffix(tree: Path) -> None:
    assert by_suffix(tree) == {"": 1, ".png": 1, ".txt": 3}


def test_total_size_and_largest(tree: Path) -> None:
    assert total_size(tree) == sum(path.stat().st_size for path in walk(tree))
    biggest = largest(tree)
    assert biggest is not None and biggest.name == "картинка.png"


def test_empty_directory(tmp_path: Path) -> None:
    assert list(walk(tmp_path)) == []
    assert by_suffix(tmp_path) == {}
    assert total_size(tmp_path) == 0
    assert largest(tmp_path) is None
    assert first(tmp_path, ".txt") is None

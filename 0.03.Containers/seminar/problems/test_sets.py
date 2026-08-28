from sets import contains_all, exclusive, only_first, shared


def test_only_first() -> None:
    assert only_first(["а", "б", "в"], ["б"]) == ["а", "в"]
    assert only_first(["а"], ["а"]) == []
    assert only_first([], ["а"]) == []


def test_only_first_drops_duplicates() -> None:
    assert only_first(["а", "а", "б"], ["б"]) == ["а"]


def test_shared() -> None:
    assert shared(["а", "б", "в"], ["б", "в", "г"]) == ["б", "в"]
    assert shared(["а"], ["б"]) == []
    assert shared([], []) == []


def test_shared_is_symmetric() -> None:
    assert shared(["а", "б"], ["б", "в"]) == shared(["б", "в"], ["а", "б"])


def test_exclusive() -> None:
    assert exclusive(["а", "б"], ["б", "в"]) == ["а", "в"]
    assert exclusive(["а"], ["а"]) == []
    assert exclusive([], ["а"]) == ["а"]


def test_contains_all() -> None:
    assert contains_all(["а", "б", "в"], ["а", "в"]) is True
    assert contains_all(["а", "б"], ["а", "г"]) is False
    assert contains_all(["а", "а"], ["а"]) is True


def test_contains_all_with_nothing_required() -> None:
    assert contains_all([], []) is True
    assert contains_all([], ["а"]) is False

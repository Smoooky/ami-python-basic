from task04_versions import Version, dedupe


def test_fields_stored() -> None:
    v = Version(3, 4)
    assert v.major == 3
    assert v.minor == 4


def test_created_counts_every_created_instance() -> None:
    # Счётчик общий для класса, поэтому сравниваем прирост, а не значение.
    before = Version.created
    Version(0, 1)
    Version(0, 2)
    assert Version.created - before == 2


def test_bump_minor_returns_new_untouched_original() -> None:
    v = Version(1, 2)
    nxt = v.bump_minor()
    assert isinstance(nxt, Version)
    assert nxt is not v
    assert nxt == Version(1, 3)
    assert v == Version(1, 2)  # исходная не изменилась


def test_bump_minor_chain() -> None:
    assert Version(1, 0).bump_minor().bump_minor() == Version(1, 2)


def test_bump_minor_counts_in_created() -> None:
    before = Version.created
    Version(9, 9).bump_minor()
    # Сам номер и новый объект из bump_minor — два создания.
    assert Version.created - before == 2


def test_equality_by_coordinates() -> None:
    assert Version(1, 2) == Version(1, 2)
    assert Version(1, 2) != Version(2, 2)
    assert Version(1, 2) != Version(1, 3)


def test_equality_with_foreign_type_is_false() -> None:
    assert (Version(1, 2) == (1, 2)) is False
    assert ((1, 2) == Version(1, 2)) is False
    assert (Version(1, 2) == "1.2") is False


def test_equal_versions_collapse_in_set() -> None:
    # Главная проверка: согласованные __eq__ и __hash__ — в set один элемент.
    assert len({Version(2, 1), Version(2, 1), Version(2, 2)}) == 2


def test_version_as_dict_key() -> None:
    releases = {Version(1, 0): "первая", Version(2, 0): "вторая"}
    assert releases[Version(1, 0)] == "первая"


def test_dedupe_keeps_first_occurrence_order() -> None:
    versions = [
        Version(1, 0),
        Version(1, 1),
        Version(1, 0),
        Version(2, 0),
        Version(1, 1),
    ]
    assert dedupe(versions) == [Version(1, 0), Version(1, 1), Version(2, 0)]


def test_dedupe_without_duplicates() -> None:
    versions = [Version(0, 1), Version(0, 2)]
    assert dedupe(versions) == versions

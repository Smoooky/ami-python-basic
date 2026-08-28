import pytest
from notebook import Notebook, PlainNotebook, Section


def test_plain_notebook() -> None:
    diary = PlainNotebook({"понедельник": "ходил на пары"})

    assert diary.read("понедельник") == "ходил на пары"
    assert diary.get("вторник") is None
    assert diary.get("вторник", "—") == "—"
    assert "понедельник" in diary
    assert len(diary) == 1
    assert diary.titles() == ["понедельник"]

    diary.write_many({"вторник": "проспал", "среда": "сдал лабу"})
    assert diary.titles() == ["вторник", "понедельник", "среда"]

    diary.erase("вторник")
    with pytest.raises(KeyError):
        diary.read("вторник")


def test_sections_share_one_notebook() -> None:
    shared = PlainNotebook()
    anya = Section(shared, "Аня: ")
    borya = Section(shared, "Боря: ")

    anya.write("домашка", "прочитать главу 3")
    borya.write("домашка", "доделать лабу")

    assert shared.titles() == ["Аня: домашка", "Боря: домашка"]
    assert anya.titles() == ["домашка"]
    assert anya.read("домашка") == "прочитать главу 3"
    assert "домашка" in borya
    assert len(anya) == 1


def test_copy_between_different_notebooks() -> None:
    shared = PlainNotebook()
    anya = Section(shared, "Аня: ")
    anya.write("домашка", "прочитать главу 3")

    my_own = PlainNotebook()
    assert anya.copy_to(my_own) == 1
    assert my_own.titles() == ["домашка"]


def test_abstract_class_cannot_be_created() -> None:
    with pytest.raises(TypeError):
        Notebook()  # type: ignore[abstract]

    class Fake(Notebook):
        pass

    with pytest.raises(TypeError):
        Fake()  # type: ignore[abstract]

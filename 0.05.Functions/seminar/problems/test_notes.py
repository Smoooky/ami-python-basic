from notes import Notebook


def test_new_notebook_is_empty() -> None:
    notebook = Notebook("Дневник")
    assert notebook.size() == 0
    assert notebook.latest() == ""


def test_add_and_size() -> None:
    notebook = Notebook("Дневник")
    notebook.add("раз")
    notebook.add("два")
    assert notebook.size() == 2
    assert notebook.latest() == "два"


def test_two_notebooks_do_not_share_entries() -> None:
    # Главная проверка: список записей создаётся в __init__, а не в теле класса.
    first = Notebook("Первая")
    second = Notebook("Вторая")
    first.add("запись")
    assert first.size() == 1
    assert second.size() == 0


def test_two_notebooks_keep_their_own_titles() -> None:
    first = Notebook("Первая")
    second = Notebook("Вторая")
    first.add("раз")
    assert first.describe() == "Первая, записей: 1"
    assert second.describe() == "Вторая, записей: 0"


def test_search() -> None:
    notebook = Notebook("Дневник")
    notebook.add("купить хлеб")
    notebook.add("купить молоко")
    notebook.add("позвонить маме")
    assert notebook.search("купить") == ["купить хлеб", "купить молоко"]
    assert notebook.search("маме") == ["позвонить маме"]


def test_search_finds_nothing() -> None:
    notebook = Notebook("Дневник")
    notebook.add("раз")
    assert notebook.search("два") == []
    assert Notebook("Пустая").search("что угодно") == []


def test_search_by_an_empty_part_returns_everything() -> None:
    notebook = Notebook("Дневник")
    notebook.add("раз")
    notebook.add("два")
    assert notebook.search("") == ["раз", "два"]


def test_method_taken_from_an_object_remembers_it() -> None:
    # Связанный метод можно взять как значение и вызвать позже.
    notebook = Notebook("Дневник")
    write = notebook.add
    write("через связанный метод")
    assert notebook.latest() == "через связанный метод"


def test_bound_methods_of_different_objects_are_different() -> None:
    first = Notebook("Первая")
    second = Notebook("Вторая")
    handlers = [first.add, second.add]
    handlers[0]("в первую")
    assert first.size() == 1
    assert second.size() == 0

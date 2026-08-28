from printing import Book


def test_repr() -> None:
    assert repr(Book("Мастер", 1967)) == "Book('Мастер', 1967)"


def test_str() -> None:
    assert str(Book("Мастер", 1967)) == "Мастер (1967)"


def test_print_uses_str() -> None:
    assert f"{Book('Мастер', 1967)}" == "Мастер (1967)"


def test_container_uses_repr() -> None:
    # Список печатает элементы через repr, а не через str.
    assert str([Book("Мастер", 1967)]) == "[Book('Мастер', 1967)]"


def test_repr_quotes_only_the_title() -> None:
    assert repr(Book("Оно", 1986)) == "Book('Оно', 1986)"

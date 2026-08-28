from format_row import format_row


def test_simple() -> None:
    assert format_row("Alice", 9.5) == "Alice           9.50"


def test_integer_score() -> None:
    assert format_row("Bob", 10) == "Bob            10.00"


def test_length_is_twenty() -> None:
    assert len(format_row("Alice", 9.5)) == 20

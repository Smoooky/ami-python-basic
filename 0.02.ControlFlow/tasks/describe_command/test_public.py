from describe_command import describe_command


def test_empty() -> None:
    assert describe_command("") == "пустая команда"


def test_quit() -> None:
    assert describe_command("quit") == "выход"


def test_move() -> None:
    assert describe_command("move 3 4") == "движение в (3, 4)"

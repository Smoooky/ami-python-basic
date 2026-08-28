from slices import every_other, head, reverse, swap_halves, trim


def test_reverse() -> None:
    assert reverse("привет") == "тевирп"
    assert reverse("а") == "а"
    assert reverse("") == ""


def test_reverse_keeps_the_first_letter() -> None:
    # Частая ошибка: text[-1:0:-1] теряет первый символ.
    assert reverse("абв") == "вба"


def test_every_other() -> None:
    assert every_other("абвгд") == "авд"
    assert every_other("абвг") == "ав"
    assert every_other("а") == "а"
    assert every_other("") == ""


def test_head() -> None:
    assert head("привет", 3) == "при"
    assert head("привет", 0) == ""
    assert head("привет", 6) == "привет"


def test_head_does_not_break_on_a_short_string() -> None:
    assert head("да", 100) == "да"
    assert head("", 5) == ""


def test_trim() -> None:
    assert trim("привет", 1) == "риве"
    assert trim("привет", 2) == "ив"
    assert trim("привет", 3) == ""


def test_trim_by_zero_returns_everything() -> None:
    assert trim("привет", 0) == "привет"
    assert trim("", 0) == ""


def test_trim_more_than_the_string_holds() -> None:
    assert trim("привет", 10) == ""


def test_swap_halves() -> None:
    assert swap_halves("абвгде") == "гдеабв"
    assert swap_halves("абвгд") == "вгдаб"
    assert swap_halves("аб") == "ба"
    assert swap_halves("") == ""


def test_swap_halves_twice_restores_even_strings() -> None:
    assert swap_halves(swap_halves("абвгде")) == "абвгде"

from shapes import command, describe, verdict


def test_describe_short_lists() -> None:
    assert describe([]) == "пусто"
    assert describe([7]) == "одно число: 7"


def test_describe_pairs() -> None:
    assert describe([3, 3]) == "два одинаковых: 3"
    assert describe([3, 5]) == "пара: 3 и 5"
    assert describe([0, 0]) == "два одинаковых: 0"


def test_describe_long_lists() -> None:
    assert describe([1, 2, 3]) == "первое 1, ещё 2"
    assert describe([9, 9, 9]) == "первое 9, ещё 2"


def test_verdict() -> None:
    assert verdict(100, 60) == "идеально"
    assert verdict(60, 60) == "зачёт"
    assert verdict(99, 60) == "зачёт"
    assert verdict(59, 60) == "незачёт"
    assert verdict(0, 60) == "не приступал"


def test_verdict_when_a_hundred_is_also_passing() -> None:
    # Сотня подходит и под "зачёт", но проверяется раньше.
    assert verdict(100, 100) == "идеально"


def test_verdict_when_zero_is_passing() -> None:
    assert verdict(0, 0) == "зачёт"


def test_command() -> None:
    assert command("стоп") == "останов"
    assert command("иди домой") == "иду в домой"
    assert command("иди") == "куда идти?"
    assert command("прыгай") == "не понял"
    assert command("") == "не понял"


def test_command_with_extra_words() -> None:
    assert command("иди домой быстро") == "не понял"
    assert command("стоп сейчас") == "не понял"

from divide import ceil_div, clock_add, same_sign, sign, split_time


def test_sign() -> None:
    assert sign(10) == 1
    assert sign(-10) == -1
    assert sign(0) == 0
    assert sign(2**100) == 1


def test_same_sign() -> None:
    assert same_sign(3, 8) is True
    assert same_sign(-3, -8) is True
    assert same_sign(-3, 8) is False
    assert same_sign(0, 5) is True
    assert same_sign(0, -5) is False


def test_ceil_div() -> None:
    assert ceil_div(7, 2) == 4
    assert ceil_div(8, 2) == 4
    assert ceil_div(9, 2) == 5
    assert ceil_div(0, 3) == 0
    assert ceil_div(-7, 2) == -3
    assert ceil_div(-8, 2) == -4


def test_ceil_div_stays_exact_on_huge_numbers() -> None:
    # Через float такое не посчитать: мантиссы не хватит.
    assert ceil_div(10**20 + 1, 10) == 10**19 + 1


def test_clock_add() -> None:
    assert clock_add(9, 3) == 12
    assert clock_add(23, 1) == 0
    assert clock_add(0, -1) == 23
    assert clock_add(10, -30) == 4
    assert clock_add(0, 240) == 0


def test_split_time() -> None:
    assert split_time(3661) == (1, 1, 1)
    assert split_time(0) == (0, 0, 0)
    assert split_time(59) == (0, 0, 59)
    assert split_time(3600) == (1, 0, 0)
    assert split_time(86399) == (23, 59, 59)


def test_split_time_beyond_a_day() -> None:
    # Сутки не ограничивают: часы просто продолжают расти.
    assert split_time(90061) == (25, 1, 1)

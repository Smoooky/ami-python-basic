from apply import compose, partial, repeat


def double(value: int) -> int:
    return value * 2


def increment(value: int) -> int:
    return value + 1


def test_compose_runs_left_to_right() -> None:
    pipeline = compose([double, increment])
    assert pipeline(3) == 7

    other = compose([increment, double])
    assert other(3) == 8


def test_compose_of_an_empty_list() -> None:
    assert compose([])(5) == 5


def test_compose_returns_a_function() -> None:
    pipeline = compose([double])
    assert callable(pipeline)
    assert pipeline(1) == 2
    assert pipeline(2) == 4


def test_partial_fills_the_first_arguments() -> None:
    def power(base: int, exponent: int) -> int:
        return int(base**exponent)

    squares = partial(power, exponent=2)
    assert squares(5) == 25

    of_two = partial(power, 2)
    assert of_two(10) == 1024


def test_partial_keeps_the_rest_open() -> None:
    def join(a: str, b: str, c: str) -> str:
        return a + b + c

    started = partial(join, "a")
    assert started("b", "c") == "abc"


def test_partial_can_be_overridden_by_name() -> None:
    def greet(name: str, greeting: str = "привет") -> str:
        return f"{greeting}, {name}"

    hello = partial(greet, greeting="здорово")
    assert hello("Аня") == "здорово, Аня"
    assert hello("Аня", greeting="салют") == "салют, Аня"


def test_repeat() -> None:
    assert repeat(double, 3)(1) == 8
    assert repeat(increment, 5)(0) == 5
    assert repeat(double, 0)(7) == 7
    assert repeat(double, -1)(7) == 7

from importlib import import_module

functions = import_module("2_functions")


def test_apply_twice() -> None:
    assert functions.apply_twice(lambda x: x + 1, 5) == 7
    assert functions.apply_twice(lambda x: x * x, 2) == 16
    assert functions.apply_twice(lambda x: 0, 5) == 0


def test_compose_applies_inner_first() -> None:
    double = lambda x: x * 2
    inc = lambda x: x + 1

    composed = functions.compose(double, inc)

    assert callable(composed)
    assert composed(5) == 12
    assert functions.compose(inc, double)(5) == 11


def test_make_scaler_closures_are_independent() -> None:
    times_three = functions.make_scaler(3)
    times_zero = functions.make_scaler(0)

    assert times_three(7) == 21
    assert times_three(-2) == -6
    assert times_zero(99) == 0


def test_call_table() -> None:
    ops = {
        "add": lambda a, b: a + b,
        "mul": lambda a, b: a * b,
    }

    assert functions.call_table(ops, "add", 2, 3) == 5
    assert functions.call_table(ops, "mul", 2, 3) == 6

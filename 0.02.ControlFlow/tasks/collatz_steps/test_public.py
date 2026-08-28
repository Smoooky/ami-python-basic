from collatz_steps import collatz_steps


def test_one_needs_no_steps() -> None:
    assert collatz_steps(1) == 0


def test_two() -> None:
    assert collatz_steps(2) == 1


def test_three() -> None:
    assert collatz_steps(3) == 7

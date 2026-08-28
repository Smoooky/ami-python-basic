from fizzbuzz import fizzbuzz


def test_five() -> None:
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fifteen_is_fizzbuzz() -> None:
    assert fizzbuzz(15)[-1] == "FizzBuzz"


def test_zero_is_empty() -> None:
    assert fizzbuzz(0) == []

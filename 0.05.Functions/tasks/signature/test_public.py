from signature import call_with, linear, mixed, move, settings


def test_linear_computes() -> None:
    assert linear(1) == 1.0
    assert linear(1, 10) == 10.0
    assert linear(2, slope=10, intercept=3) == 23.0


def test_settings_are_passed_by_name() -> None:
    assert settings(host="localhost") == "localhost:80"
    assert settings(host="localhost", port=8080) == "localhost:8080"


def test_mixed() -> None:
    assert mixed(1) == 1
    assert mixed(1, 2) == 3
    assert mixed(1, 2, c=3) == 6


def test_positional_only_frees_the_name() -> None:
    # distance стоит до /, поэтому имя "distance" свободно для options.
    # Без разделителя такой вызов вообще не собрался бы.
    assert move(5) == (5, {})
    assert move(5, distance="fast") == (5, {"distance": "fast"})
    assert move(5, speed=2, distance="fast") == (5, {"speed": 2, "distance": "fast"})


def test_call_with_unpacks() -> None:
    assert call_with(linear, [2], {"slope": 3}) == 6.0
    assert call_with(settings, [], {"host": "a", "port": 1}) == "a:1"
    assert call_with(mixed, [1, 2], {"c": 3}) == 6
    assert call_with(move, [5], {"distance": "fast"}) == (5, {"distance": "fast"})

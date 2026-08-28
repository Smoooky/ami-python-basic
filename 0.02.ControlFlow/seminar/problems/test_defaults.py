from defaults import clamp, first_filled, label, setting


def test_label() -> None:
    assert label("Иван") == "Иван"
    assert label("") == "аноним"
    assert label(" ") == " "


def test_setting_takes_the_default_when_there_is_no_value() -> None:
    assert setting(None, 8080) == 8080
    assert setting(443, 8080) == 443


def test_setting_keeps_a_zero() -> None:
    # Ноль ложен, но это осмысленное значение: подменять его нельзя.
    assert setting(0, 8080) == 0


def test_first_filled() -> None:
    assert first_filled(["", "", "третья"], "-") == "третья"
    assert first_filled(["первая", "вторая"], "-") == "первая"
    assert first_filled(["", ""], "-") == "-"
    assert first_filled([], "-") == "-"


def test_clamp() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-3, 0, 10) == 0
    assert clamp(42, 0, 10) == 10
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_clamp_on_negative_bounds() -> None:
    assert clamp(-5, -10, -1) == -5
    assert clamp(0, -10, -1) == -1

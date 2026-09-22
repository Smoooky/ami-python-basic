from task01_pipeline import apply_each, fuse, partial_apply, thread


def test_apply_each_maps_every_function() -> None:
    assert apply_each([lambda x: x + 1, lambda x: x * 2], 10) == [11, 20]


def test_apply_each_empty() -> None:
    assert apply_each([], "а") == []


def test_thread_chains_left_to_right() -> None:
    # Главная проверка: сначала +1, потом *2 (а не наоборот).
    assert thread(10, [lambda x: x + 1, lambda x: x * 2]) == 22


def test_thread_empty_returns_value() -> None:
    assert thread([1, 2], []) == [1, 2]


def test_partial_apply_fixes_positionals_first() -> None:
    power_of_two = partial_apply(pow, 2)
    assert power_of_two(10) == 1024


def test_partial_apply_keyword_overrides() -> None:
    def greet(name: str, punct: str = "!") -> str:
        return f"Привет, {name}{punct}"

    shout = partial_apply(greet, punct="!!!")
    assert shout("мир") == "Привет, мир!!!"
    # Главная проверка: новый именованный перекрывает зафиксированный.
    assert shout("мир", punct="?") == "Привет, мир?"


def test_partial_apply_mixes_positional_and_keyword() -> None:
    def f(a: int, b: int, c: int = 3, d: int = 4) -> tuple[int, int, int, int]:
        return (a, b, c, d)

    g = partial_apply(f, 1, d=40)
    assert g(2) == (1, 2, 3, 40)
    assert g(2, c=30) == (1, 2, 30, 40)


def test_fuse_applies_in_order() -> None:
    assert fuse(lambda x: x + 1, lambda x: x * 10)(1) == 20


def test_fuse_empty_is_identity() -> None:
    identity = fuse()
    assert identity([1]) == [1]
    assert identity("аб") == "аб"


def test_fuse_of_three() -> None:
    trim_upper_cut = fuse(str.strip, str.upper, lambda s: s[:3])
    assert trim_upper_cut("  привет  ") == "ПРИ"

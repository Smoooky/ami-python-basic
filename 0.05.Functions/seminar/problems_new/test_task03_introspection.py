from task03_introspection import accepts_star, defaults_table, param_count, short_signature


def fa(x, /, y=1, *, z=2):
    return x + y + z


def fb(a, *args, **kw):
    return a


def fc():
    return None


def fd(*, debug=False):
    return debug


def fe(a, b=1, /, c=2, *, d=3, e):
    return a


def fg(greet="hi"):
    return greet


def test_param_count() -> None:
    assert param_count(fa) == 3
    assert param_count(fb) == 1  # *args и **kwargs не считаются
    assert param_count(fc) == 0
    assert param_count(fd) == 1
    assert param_count(fe) == 5


def test_defaults_table_plain_and_kwonly() -> None:
    assert defaults_table(fa) == {"y": 1, "z": 2}
    assert defaults_table(fd) == {"debug": False}
    assert defaults_table(fg) == {"greet": "hi"}


def test_defaults_table_tail_alignment() -> None:
    # Главная проверка: __defaults__ ложится на хвост позиционных: b=1, c=2.
    assert defaults_table(fe) == {"b": 1, "c": 2, "d": 3}


def test_defaults_table_empty() -> None:
    assert defaults_table(fb) == {}
    assert defaults_table(fc) == {}


def test_accepts_star() -> None:
    assert accepts_star(fb) == (True, True)
    assert accepts_star(fa) == (False, False)
    assert accepts_star(fd) == (False, False)


def test_short_signature_with_separators() -> None:
    assert short_signature(fa) == "fa(x, /, y=1, *, z=2)"
    assert short_signature(fe) == "fe(a, b=1, /, c=2, *, d=3, e)"


def test_short_signature_with_star_args() -> None:
    assert short_signature(fb) == "fb(a, *args, **kw)"


def test_short_signature_no_params() -> None:
    assert short_signature(fc) == "fc()"


def test_short_signature_kwonly_without_args() -> None:
    # Главная проверка: именованные без *args — звёздочка сама по себе.
    assert short_signature(fd) == "fd(*, debug=False)"


def test_short_signature_repr_of_defaults() -> None:
    # Главная проверка: дефолт в repr-виде — кавычки у строк.
    assert short_signature(fg) == "fg(greet='hi')"

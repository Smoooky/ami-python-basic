import pytest
from error_chain import error_chain, explain, root_cause


def raise_with_cause() -> None:
    try:
        raise ZeroDivisionError("деление на ноль")
    except ZeroDivisionError as error:
        raise ValueError("плохой делитель") from error


def raise_inside_handler() -> None:
    try:
        raise KeyError("host")
    except KeyError:
        raise RuntimeError("обработчик сам сломался")  # noqa: B904


def raise_with_hidden_context() -> None:
    try:
        raise KeyError("host")
    except KeyError:
        raise RuntimeError("наружу показываем только это") from None


def test_chain_follows_cause() -> None:
    with pytest.raises(ValueError) as info:
        raise_with_cause()

    chain = error_chain(info.value)
    assert len(chain) == 2
    assert chain[0] is info.value
    assert isinstance(chain[1], ZeroDivisionError)


def test_root_cause() -> None:
    with pytest.raises(ValueError) as info:
        raise_with_cause()
    assert isinstance(root_cause(info.value), ZeroDivisionError)

    lonely = ValueError("одиночка")
    assert root_cause(lonely) is lonely


def test_explain_marks_the_kind_of_link() -> None:
    with pytest.raises(ValueError) as caused:
        raise_with_cause()
    assert explain(caused.value) == (
        "ValueError: плохой делитель\n  причина: ZeroDivisionError: деление на ноль"
    )

    with pytest.raises(RuntimeError) as contextual:
        raise_inside_handler()
    assert explain(contextual.value) == (
        "RuntimeError: обработчик сам сломался\n  в процессе: KeyError: 'host'"
    )


def test_suppressed_context_breaks_the_chain() -> None:
    with pytest.raises(RuntimeError) as info:
        raise_with_hidden_context()

    assert error_chain(info.value) == [info.value]
    assert explain(info.value) == "RuntimeError: наружу показываем только это"

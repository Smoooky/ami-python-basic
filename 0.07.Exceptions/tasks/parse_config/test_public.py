import pytest
from parse_config import (
    BadKeyError,
    BadValueError,
    ConfigError,
    DuplicateKeyError,
    LineError,
    MissingEqualsError,
    check_config,
    parse_config,
)

BROKEN = [
    "host = localhost",
    "просто текст",
    "Port = 80",
    "host = 127.0.0.1",
    "timeout =",
]


def test_parses_a_clean_config() -> None:
    config = parse_config(
        [
            "# сеть",
            "host = localhost",
            "port = 8080",
            "debug = false",
            "",
            "motd = добро пожаловать",
        ]
    )
    assert config == {
        "host": "localhost",
        "port": 8080,
        "debug": False,
        "motd": "добро пожаловать",
    }


def test_value_may_contain_equals() -> None:
    assert parse_config(["formula = a=b+c"]) == {"formula": "a=b+c"}


def test_only_lowercase_booleans() -> None:
    assert parse_config(["mode = True"]) == {"mode": "True"}


def test_check_config_reports_every_line() -> None:
    errors = check_config(BROKEN)
    assert [type(error) for error in errors] == [
        MissingEqualsError,
        BadKeyError,
        DuplicateKeyError,
        BadValueError,
    ]
    assert [error.line for error in errors] == [2, 3, 4, 5]


def test_strict_mode_raises_with_all_errors() -> None:
    with pytest.raises(ConfigError) as info:
        parse_config(BROKEN)

    assert str(info.value) == "ошибок в конфиге: 4"
    assert len(info.value.errors) == 4
    assert isinstance(info.value.errors[0], LineError)
    assert info.value.__cause__ is info.value.errors[0]


def test_lenient_mode_keeps_what_it_can() -> None:
    assert parse_config(BROKEN, strict=False) == {"host": "localhost"}

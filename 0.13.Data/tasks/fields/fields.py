QUOTE = '"'
COMMA = ","

# Символы, из-за которых поле приходится брать в кавычки.
SPECIAL = ',"\r\n'

# Состояния автомата.
START = "НАЧАЛО"
PLAIN = "ПРОСТОЕ"
QUOTED = "В КАВЫЧКАХ"
AFTER_QUOTE = "ПОСЛЕ КАВЫЧКИ"


def needs_quotes(field: str) -> bool:
    raise NotImplementedError("Implement me")


def quote(field: str) -> str:
    raise NotImplementedError("Implement me")


def unquote(field: str) -> str:
    raise NotImplementedError("Implement me")


def join_row(fields: list[str]) -> str:
    raise NotImplementedError("Implement me")


def dump(rows: list[list[str]]) -> str:
    raise NotImplementedError("Implement me")


def parse(text: str) -> list[list[str]]:
    raise NotImplementedError("Implement me")

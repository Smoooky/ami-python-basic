# Цифры индекса перечислены явно: str.isdigit() принимает и "²", и восточные
# цифры, а int() их потом не берёт.
DIGITS = "0123456789"


def escape(token: str) -> str:
    raise NotImplementedError("Implement me")


def unescape(token: str) -> str:
    raise NotImplementedError("Implement me")


def parse(pointer: str) -> list[str]:
    raise NotImplementedError("Implement me")


def resolve(document: object, pointer: str) -> object:
    raise NotImplementedError("Implement me")


def exists(document: object, pointer: str) -> bool:
    raise NotImplementedError("Implement me")


def set_value(document: object, pointer: str, value: object) -> object:
    raise NotImplementedError("Implement me")


def pointers(document: object) -> list[str]:
    raise NotImplementedError("Implement me")

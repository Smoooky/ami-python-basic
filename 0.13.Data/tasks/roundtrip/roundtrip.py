import json

# Значения, у которых в JSON своя запись, не совпадающая с str().
NAMED = {True: "true", False: "false", None: "null"}


def as_key(key: object) -> str:
    raise NotImplementedError("Implement me")


def key_conflicts(mapping: dict[object, object]) -> list[str]:
    raise NotImplementedError("Implement me")


def restored(value: object) -> object:
    raise NotImplementedError("Implement me")


def survives(value: object) -> bool:
    raise NotImplementedError("Implement me")

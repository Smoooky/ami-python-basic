# Символы, у которых в JSON есть короткая запись.
ESCAPES = {
    '"': '\\"',
    "\\": "\\\\",
    "\n": "\\n",
    "\r": "\\r",
    "\t": "\\t",
    "\b": "\\b",
    "\f": "\\f",
}


def dump_string(text: str) -> str:
    raise NotImplementedError("Implement me")


def dumps(value: object) -> str:
    raise NotImplementedError("Implement me")


def dumps_sorted(value: object) -> str:
    raise NotImplementedError("Implement me")

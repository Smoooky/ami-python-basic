from collections import OrderedDict
from typing import Any


class Recent:
    """Список недавних: помнит не больше `capacity` записей."""

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError("Implement me")

    def put(self, key: str, value: Any) -> str | None:
        raise NotImplementedError("Implement me")

    def get(self, key: str, default: Any = None) -> Any:
        raise NotImplementedError("Implement me")

    def forget(self, key: str) -> None:
        raise NotImplementedError("Implement me")

    def keys(self) -> list[str]:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __contains__(self, key: object) -> bool:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")

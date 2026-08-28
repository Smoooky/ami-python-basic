def error_chain(error: BaseException) -> list[BaseException]:
    raise NotImplementedError("Implement me")


def root_cause(error: BaseException) -> BaseException:
    raise NotImplementedError("Implement me")


def explain(error: BaseException) -> str:
    raise NotImplementedError("Implement me")

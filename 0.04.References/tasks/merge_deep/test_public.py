from merge_deep import merge_deep


def test_disjoint_keys() -> None:
    assert merge_deep({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_nested_merge() -> None:
    base = {"db": {"host": "localhost", "port": 5432}}
    patch = {"db": {"port": 5433}}
    assert merge_deep(base, patch) == {"db": {"host": "localhost", "port": 5433}}


def test_non_dict_replaces_whole_section() -> None:
    assert merge_deep({"db": {"host": "localhost"}}, {"db": "off"}) == {"db": "off"}

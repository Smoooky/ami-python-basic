import inspect

import pytest
from tally import feed, leaders, tally


def test_tally_starts_empty() -> None:
    counter = tally()
    assert next(counter) == {}


def test_tally_counts_what_it_is_sent() -> None:
    counter = tally()
    next(counter)
    assert counter.send("аня") == {"аня": 1}
    assert counter.send("боря") == {"аня": 1, "боря": 1}
    assert counter.send("аня") == {"аня": 2, "боря": 1}


def test_none_finishes_the_counter() -> None:
    counter = tally()
    next(counter)
    counter.send("аня")
    with pytest.raises(StopIteration):
        counter.send(None)


def test_every_snapshot_is_a_new_dict() -> None:
    counter = tally()
    empty = next(counter)
    after = counter.send("аня")

    assert empty is not after
    assert empty == {}
    counter.send("аня")
    assert after == {"аня": 1}


def test_feed() -> None:
    assert feed(["аня", "боря", "аня"]) == {"аня": 2, "боря": 1}
    assert feed([]) == {}
    assert feed(["аня"]) == {"аня": 1}


def test_leaders() -> None:
    assert list(leaders(["аня", "боря", "аня"])) == ["аня", None, "аня"]
    assert list(leaders([])) == []
    assert inspect.isgenerator(leaders(["аня"]))

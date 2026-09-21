from importlib import import_module

buffer_tasks = import_module("5_buffer")


def test_histogram_counts_bytes() -> None:
    counts = buffer_tasks.histogram(memoryview(bytearray([1, 1, 250, 0])))

    assert len(counts) == 256
    assert counts[0] == 1
    assert counts[1] == 2
    assert counts[250] == 1
    assert counts[2] == 0
    assert sum(counts) == 4


def test_histogram_of_a_window() -> None:
    data = bytearray([1, 2, 3, 2])

    counts = buffer_tasks.histogram(memoryview(data)[1:])

    assert counts[2] == 2
    assert counts[3] == 1
    assert counts[1] == 0


def test_mirror_window_even_length() -> None:
    data = bytearray(b"abcdef")

    buffer_tasks.mirror_window(memoryview(data))

    assert bytes(data) == b"fedcba"


def test_mirror_window_odd_length() -> None:
    data = bytearray(b"abcde")

    buffer_tasks.mirror_window(memoryview(data))

    assert bytes(data) == b"edcba"


def test_mirror_window_touches_only_the_window() -> None:
    data = bytearray(b"abcdef")

    buffer_tasks.mirror_window(memoryview(data)[1:5])

    assert bytes(data) == b"aedcbf"


def test_most_common() -> None:
    assert buffer_tasks.most_common(memoryview(bytearray([7, 7, 7, 2]))) == 7


def test_most_common_tie_returns_the_smallest_byte() -> None:
    assert buffer_tasks.most_common(memoryview(bytearray([9, 5, 9, 5]))) == 5

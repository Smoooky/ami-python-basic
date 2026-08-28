from window import chunk, copy_chunk, is_shared, overwrite, total


def sample() -> bytearray:
    return bytearray([10, 20, 30, 40, 50])


def test_chunk_is_a_window_not_a_copy() -> None:
    data = sample()
    window = chunk(data, 1, 3)

    assert isinstance(window, memoryview)
    assert list(window) == [20, 30, 40]

    data[1] = 99
    assert list(window) == [99, 30, 40]


def test_copy_chunk_is_a_copy() -> None:
    data = sample()
    piece = copy_chunk(data, 1, 3)

    assert isinstance(piece, bytearray)
    assert list(piece) == [20, 30, 40]

    data[1] = 99
    assert list(piece) == [20, 30, 40]


def test_total() -> None:
    data = sample()
    assert total(chunk(data, 0, 5)) == 150
    assert total(chunk(data, 1, 2)) == 50
    assert total(chunk(data, 0, 0)) == 0


def test_overwrite_changes_the_buffer() -> None:
    data = sample()
    window = chunk(data, 1, 3)
    overwrite(window, [1, 2, 3])

    assert list(data) == [10, 1, 2, 3, 50]


def test_is_shared() -> None:
    data = sample()
    other = sample()

    assert is_shared(chunk(data, 0, 2), data) is True
    assert is_shared(chunk(data, 0, 2), other) is False
    assert is_shared(memoryview(other), other) is True


def test_a_copy_is_not_shared_with_anyone() -> None:
    data = sample()
    piece = copy_chunk(data, 0, 3)

    assert is_shared(memoryview(piece), data) is False
    assert is_shared(memoryview(piece), piece) is True

from vector import Vector


def test_fields() -> None:
    v = Vector(3, 4)
    assert v.x == 3
    assert v.y == 4


def test_length() -> None:
    assert Vector(3, 4).length() == 5.0


def test_equality() -> None:
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(2, 1)

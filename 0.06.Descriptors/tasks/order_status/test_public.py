from order_status import OrderStatus


def test_allowed_transition() -> None:
    assert OrderStatus.NEW.can_move_to(OrderStatus.PAID) is True
    assert OrderStatus.NEW.can_move_to(OrderStatus.DELIVERED) is False


def test_is_final() -> None:
    assert OrderStatus.DELIVERED.is_final() is True
    assert OrderStatus.NEW.is_final() is False


def test_valid_path() -> None:
    path = [OrderStatus.NEW, OrderStatus.PAID, OrderStatus.DELIVERED]
    assert OrderStatus.is_valid_path(path) is True

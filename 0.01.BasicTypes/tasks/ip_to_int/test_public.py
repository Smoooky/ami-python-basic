from ip_to_int import ip_to_int


def test_zero() -> None:
    assert ip_to_int("0.0.0.0") == 0


def test_last_octet() -> None:
    assert ip_to_int("0.0.0.1") == 1


def test_private_address() -> None:
    assert ip_to_int("192.168.1.1") == 3232235777

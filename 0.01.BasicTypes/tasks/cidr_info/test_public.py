from cidr_info import cidr_info


def test_class_c() -> None:
    assert cidr_info("192.168.1.0/24") == (3232235776, 3232236031, 256)


def test_class_a() -> None:
    assert cidr_info("10.0.0.0/8") == (167772160, 184549375, 16777216)


def test_single_host() -> None:
    assert cidr_info("192.168.1.7/32") == (3232235783, 3232235783, 1)

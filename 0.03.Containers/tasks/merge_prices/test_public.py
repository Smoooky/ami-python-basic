from merge_prices import merge_prices


def test_disjoint() -> None:
    assert merge_prices({"хлеб": 50}, {"молоко": 80}) == {"хлеб": 50, "молоко": 80}


def test_update_wins() -> None:
    assert merge_prices({"хлеб": 50}, {"хлеб": 60}) == {"хлеб": 60}


def test_empty() -> None:
    assert merge_prices({}, {}) == {}

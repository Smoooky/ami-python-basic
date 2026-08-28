import pytest
from deck import Dealer, Deck, is_iterable, is_iterator

CARDS = ["туз", "король", "дама"]


def test_deck_can_be_walked_many_times() -> None:
    deck = Deck(CARDS)
    assert list(deck) == CARDS
    assert list(deck) == CARDS
    assert len(deck) == 3


def test_dealer_is_one_shot() -> None:
    dealer = iter(Deck(CARDS))
    assert list(dealer) == CARDS
    assert list(dealer) == []


def test_dealer_counts_and_stops() -> None:
    dealer = Dealer(["туз", "король"])
    assert dealer.dealt == 0
    assert next(dealer) == "туз"
    assert dealer.dealt == 1
    assert next(dealer) == "король"
    with pytest.raises(StopIteration):
        next(dealer)
    assert dealer.dealt == 2


def test_iter_of_an_iterator_is_itself() -> None:
    deck = Deck(CARDS)
    dealer = iter(deck)
    assert iter(dealer) is dealer
    assert iter(deck) is not iter(deck)


def test_deck_is_not_an_iterator() -> None:
    assert hasattr(Deck, "__next__") is False

    deck = Deck(CARDS)
    assert is_iterable(deck) is True
    assert is_iterator(deck) is False
    assert is_iterator(iter(deck)) is True


def test_checks_on_builtins() -> None:
    assert is_iterable([1, 2]) is True
    assert is_iterable("строка") is True
    assert is_iterable(42) is False

    assert is_iterator([1, 2]) is False
    assert is_iterator(iter([1, 2])) is True
    assert is_iterator(42) is False

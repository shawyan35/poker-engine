import pytest
from poker.deck import Deck
from poker.card import Card, Rank, Suit

deck = Deck()

def test_length():
    assert len(deck) == 52

def test_uniqueness():
    assert len(set(deck)) == len(deck)

def test_deal_five():
    deck = Deck()

    dealt_cards = deck.deal(5)

    assert len(dealt_cards) == 5
    assert len(deck.cards) == 47

def test_empty_deal():
    deck = Deck()

    with pytest.raises(ValueError, match="Not enough cards left in the deck"):
        deck.deal(53)

    
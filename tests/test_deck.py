import pytest
from poker.deck import Deck
from poker.card import Card, Rank, Suit

deck = Deck()

def test_length():
    assert len(Deck) == 52

def test_uniqueness():
    assert len(set(deck) == len(deck))

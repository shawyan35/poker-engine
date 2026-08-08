from enum import IntEnum
from poker.card import Card, Rank, Suit
from collections import Counter

class HandRank(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7 
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

def evaluate(cards: list[Card]) -> tuple[HandRank, list[int]]:
    """Evaluates hand strength"""
    pass

def _check_flush(cards: list[Card]) -> tuple[HandRank, list[int]] | None:
    suit_counts = Counter(card.suit for card in cards)

    for suit, count in suit_counts.items():
        if count >= 5:
            flush_cards = [card for card in cards if card.suit == suit]

            sorted_cards = sorted(flush_cards, key = lambda c: c.rank, reverse=True)[:5]
            return (HandRank.FLUSH, [c.rank for c in sorted_cards])
        
    return None

def _check_straight(cards: list[Card]) -> tuple[HandRank, list[int]] | None:
    
    unique_ranks = sorted(set(card.rank for card in cards), reverse=True)

    if len(unique_ranks) < 5:
        return None
    
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i] - unique_ranks[i+4] == 4:
            return (HandRank.STRAIGHT, unique_ranks[i:i+5])
   
    ace_low_straight = {14, 2, 3, 4, 5}
    if ace_low_straight.issubset(set(unique_ranks)):
        return (HandRank.STRAIGHT, [5, 4, 3, 2, 1])
    
    return None
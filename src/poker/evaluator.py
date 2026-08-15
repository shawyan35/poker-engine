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
    result = _check_straight_flush(cards)
    if result:
        return result
    
    result = _check_four_of_a_kind(cards)
    if result:
        return result
    
    result = _check_full_house(cards)
    if result:
        return result
    
    result = _check_flush(cards)
    if result:
        return result
    
    result = _check_straight(cards)
    if result:
        return result
    
    result = _check_three_of_a_kind(cards)
    if result:
        return result
    
    result = _check_two_pair(cards)
    if result:
        return result
    
    result = _check_one_pair(cards)
    if result:
        return result
    
    result = _check_high_card(cards)
    return result


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

def _check_four_of_a_kind(cards: list[Card]) -> tuple[HandRank, list[int]] | None:

    rank_counts = Counter(card.rank for card in cards)
    frequencies = sorted(rank_counts.values(), reverse=True)

    if frequencies[0] == 4:
        quads_rank = [rank for rank, count in rank_counts.items() if count == 4][0]
        kickers = sorted([rank for rank, count in rank_counts.items() if count != 4], reverse=True)

        return(HandRank.FOUR_OF_A_KIND, [quads_rank, kickers[0]])
    
    return None

def _check_full_house(cards: list[Card]) -> tuple[HandRank, list[int]] | None:

    rank_counts = Counter(card.rank for card in cards)
    frequencies = sorted(rank_counts.values(), reverse=True)

    if frequencies[0] == 3 and frequencies[1] >= 2:
        three_of_a_kind_rank = [rank for rank, count in rank_counts.items() if count == 3][0]
        pair_rank = [rank for rank, count in rank_counts.items() if count >= 2 and rank != three_of_a_kind_rank][0]

        return(HandRank.FULL_HOUSE, [three_of_a_kind_rank, pair_rank])
    
    return None

def _check_three_of_a_kind(cards: list[Card]) -> tuple[HandRank, list[int]] | None:

    rank_counts = Counter(card.rank for card in cards)
    frequencies = sorted(rank_counts.values(), reverse=True)

    if frequencies[0] == 3 and frequencies[1] != 2:
        three_of_a_kind_rank = [rank for rank, count in rank_counts.items() if count == 3][0]
        kickers = sorted([rank for rank, count in rank_counts.items() if count != 3], reverse=True)

        return(HandRank.THREE_OF_A_KIND, [three_of_a_kind_rank, kickers[0], kickers[1]])
   
    return None

def _check_two_pair(cards: list[Card]) -> tuple[HandRank, list[int]] | None:
    rank_counts = Counter(card.rank for card in cards)
    frequencies = sorted(rank_counts.values(), reverse=True)

    if frequencies[:2] == [2,2]:
        pair_ranks = sorted([rank for rank, count in rank_counts.items() if count == 2], reverse=True)
        kickers = sorted([rank for rank, count in rank_counts.items() if count != 2], reverse=True)

        return(HandRank.TWO_PAIR, [pair_ranks[0], pair_ranks[1], kickers[0]])
    
    return None


def _check_one_pair(cards: list[Card]) -> tuple[HandRank, list[int]] | None:
    rank_counts = Counter(card.rank for card in cards)
    frequencies = sorted(rank_counts.values(), reverse=True)

    if frequencies[0] == 2:
        pair_rank = [rank for rank, count in rank_counts.items() if count == 2][0]
        kickers = sorted([rank for rank, count in rank_counts.items() if count != 2], reverse=True)

        return(HandRank.ONE_PAIR, [pair_rank] + kickers[:3])
    
    return None

def _check_straight_flush(cards: list[Card]) -> tuple[HandRank, list[int]] | None:
    if _check_flush(cards) is None:
        return None
    suit_counts = Counter(card.suit for card in cards)

    for suit, count in suit_counts.items():
        if count >= 5:
            flush_cards = [card for card in cards if card.suit == suit]

            straight_result = _check_straight(flush_cards)
        
            if straight_result is None:
                return None
            else:
                return (HandRank.STRAIGHT_FLUSH, straight_result[1])
    
    return None
            

def _check_high_card(cards: list[Card]) -> tuple[HandRank, list[int]] | None:

    top_ranks = sorted((card.rank for card in cards), reverse=True)[:5]
    
    return (HandRank.HIGH_CARD, top_ranks)

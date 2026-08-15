from poker.montecarlo import simulate
from poker.card import Suit, Rank, Card

def test_montecarlo_sim():
    hand1 = [Card(Rank.ACE, Suit.SPADE), Card(Rank.ACE, Suit.CLUB)]
    hand2 = [Card(Rank.TWO, Suit.SPADE), Card(Rank.TWO, Suit.CLUB)]

    result = simulate(hand1, hand2, [], 10000)
    assert 75 < result[0] < 95

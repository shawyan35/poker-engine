from poker.card import Card, Rank, Suit
from poker.evaluator import HandRank, _check_flush

card1 = Card(Rank.ACE, Suit.SPADE)
card2 = Card(Rank.FIVE, Suit.SPADE)
card3 = Card(Rank.KING, Suit.SPADE)
card4 = Card(Rank.JACK, Suit.SPADE)
card5 = Card(Rank.THREE, Suit.SPADE)
card6 = Card(Rank.FIVE, Suit.DIAMOND)
card7 = Card(Rank.ACE, Suit.DIAMOND)
card8 = Card(Rank.TEN, Suit.CLUB)

def test_flush_detection():

    cards = [card1, card2, card3, card4, card5, card6, card7]
    result = _check_flush(cards)

    assert result[0] == HandRank.FLUSH
    assert result[1] == [14,13,11,5,3]

def test_no_flush():

    cards2 = [card8, card2, card3, card4, card5, card6, card7]

    result2 = _check_flush(cards2)  

    assert result2 is None
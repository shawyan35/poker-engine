from poker.card import Card, Rank, Suit
from poker.evaluator import HandRank, _check_flush, _check_straight

card1 = Card(Rank.ACE, Suit.SPADE) # Ace straight
card2 = Card(Rank.FIVE, Suit.SPADE) # Ace straight
card3 = Card(Rank.KING, Suit.SPADE) # straight
card4 = Card(Rank.JACK, Suit.SPADE) # straight
card5 = Card(Rank.THREE, Suit.SPADE) # Ace straight
card6 = Card(Rank.FIVE, Suit.DIAMOND) 
card7 = Card(Rank.ACE, Suit.DIAMOND)
card8 = Card(Rank.TEN, Suit.CLUB) # straight
card9 = Card(Rank.TWO, Suit.HEART) # Ace straight
card10 = Card(Rank.FOUR, Suit.HEART) # Ace straight
card11 = Card(Rank.NINE, Suit.HEART) # straight
card12 =Card(Rank.QUEEN, Suit.CLUB) # straight

def test_flush_detection():

    flush_cards = [card1, card2, card3, card4, card5, card6, card7]
    result = _check_flush(flush_cards)

    assert result[0] == HandRank.FLUSH
    assert result[1] == [14,13,11,5,3]

def test_no_flush():

    no_flush_cards = [card8, card2, card3, card4, card5, card6, card7]

    result2 = _check_flush(no_flush_cards)  

    assert result2 is None

def test_ace_straight():
    ace_straight_cards = [card1, card2, card5, card9, card10]
    result3 = _check_straight(ace_straight_cards)
    assert result3[0] == HandRank.STRAIGHT
    assert result3[1] == [5, 4, 3, 2, 1]

def test_straight():
    straight_cards = [card3, card4, card8, card11, card12]
    result4 = _check_straight(straight_cards)
    assert result4[0] == HandRank.STRAIGHT
    assert result4[1] == [13, 12, 11, 10, 9]
def test_no_straight():
    no_straight_cards = [card1, card2, card3, card4, card6]
    result5 = _check_straight(no_straight_cards)
    assert result5 is None



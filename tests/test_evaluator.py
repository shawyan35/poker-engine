from poker.card import Card, Rank, Suit
from poker.evaluator import HandRank, _check_flush, _check_straight, evaluate

# Spades
card1 = Card(Rank.ACE, Suit.SPADE)
card2 = Card(Rank.TWO, Suit.SPADE)
card3 = Card(Rank.THREE, Suit.SPADE)
card4 = Card(Rank.FOUR, Suit.SPADE)
card5 = Card(Rank.FIVE, Suit.SPADE)
card6 = Card(Rank.SIX, Suit.SPADE)
card7 = Card(Rank.SEVEN, Suit.SPADE)
card8 = Card(Rank.EIGHT, Suit.SPADE)
card9 = Card(Rank.NINE, Suit.SPADE)
card10 = Card(Rank.TEN, Suit.SPADE)
card11 = Card(Rank.JACK, Suit.SPADE)
card12 = Card(Rank.QUEEN, Suit.SPADE)
card13 = Card(Rank.KING, Suit.SPADE)

# Hearts
card14 = Card(Rank.ACE, Suit.HEART)
card15 = Card(Rank.TWO, Suit.HEART)
card16 = Card(Rank.THREE, Suit.HEART)
card17 = Card(Rank.FOUR, Suit.HEART)
card18 = Card(Rank.FIVE, Suit.HEART)
card19 = Card(Rank.SIX, Suit.HEART)
card20 = Card(Rank.SEVEN, Suit.HEART)
card21 = Card(Rank.EIGHT, Suit.HEART)
card22 = Card(Rank.NINE, Suit.HEART)
card23 = Card(Rank.TEN, Suit.HEART)
card24 = Card(Rank.JACK, Suit.HEART)
card25 = Card(Rank.QUEEN, Suit.HEART)
card26 = Card(Rank.KING, Suit.HEART)

# Diamonds
card27 = Card(Rank.ACE, Suit.DIAMOND)
card28 = Card(Rank.TWO, Suit.DIAMOND)
card29 = Card(Rank.THREE, Suit.DIAMOND)
card30 = Card(Rank.FOUR, Suit.DIAMOND)
card31 = Card(Rank.FIVE, Suit.DIAMOND)
card32 = Card(Rank.SIX, Suit.DIAMOND)
card33 = Card(Rank.SEVEN, Suit.DIAMOND)
card34 = Card(Rank.EIGHT, Suit.DIAMOND)
card35 = Card(Rank.NINE, Suit.DIAMOND)
card36 = Card(Rank.TEN, Suit.DIAMOND)
card37 = Card(Rank.JACK, Suit.DIAMOND)
card38 = Card(Rank.QUEEN, Suit.DIAMOND)
card39 = Card(Rank.KING, Suit.DIAMOND)

# Clubs
card40 = Card(Rank.ACE, Suit.CLUB)
card41 = Card(Rank.TWO, Suit.CLUB)
card42 = Card(Rank.THREE, Suit.CLUB)
card43 = Card(Rank.FOUR, Suit.CLUB)
card44 = Card(Rank.FIVE, Suit.CLUB)
card45 = Card(Rank.SIX, Suit.CLUB)
card46 = Card(Rank.SEVEN, Suit.CLUB)
card47 = Card(Rank.EIGHT, Suit.CLUB)
card48 = Card(Rank.NINE, Suit.CLUB)
card49 = Card(Rank.TEN, Suit.CLUB)
card50 = Card(Rank.JACK, Suit.CLUB)
card51 = Card(Rank.QUEEN, Suit.CLUB)
card52 = Card(Rank.KING, Suit.CLUB)

## FLUSH TESTS
def test_flush_detection():

    flush_cards = [card1, card13, card11, card5, card3, card47, card17]
    result = _check_flush(flush_cards)

    assert result[0] == HandRank.FLUSH
    assert result[1] == [14,13,11,5,3]

def test_no_flush():

    no_flush_cards = [card18, card24, card39, card4, card52, card6, card23]

    result = _check_flush(no_flush_cards)  

    assert result is None


## STRAIGHT TESTS
def test_ace_straight():
    ace_straight_cards = [card14, card2, card3, card17, card44]
    result = _check_straight(ace_straight_cards)
    assert result[0] == HandRank.STRAIGHT
    assert result[1] == [5, 4, 3, 2, 1]

def test_straight():
    straight_cards = [card13, card38, card11, card23, card9]
    result = _check_straight(straight_cards)
    assert result[0] == HandRank.STRAIGHT
    assert result[1] == [13, 12, 11, 10, 9]

def test_no_straight():
    no_straight_cards = [card1, card14, card33, card42, card16]
    result = _check_straight(no_straight_cards)
    assert result is None

## QUADS TESTS

def test_quads():
    quads_cards = [card1, card14, card27, card40, card2, card45, card18]
    result = evaluate(quads_cards)

    assert result[0] == HandRank.FOUR_OF_A_KIND
    assert result[1] == [14, 6]

def test_quads2():
    quads_cards = [card3, card16, card29, card42, card5, card47, card20]
    result = evaluate(quads_cards)

    assert result[0] == HandRank.FOUR_OF_A_KIND
    assert result[1] == [3, 8]

def test_no_quads():
    quads_cards = [card4, card13, card29, card42, card5, card47, card20]
    result = evaluate(quads_cards)

    assert result != HandRank.FOUR_OF_A_KIND

## FULL HOUSE TESTS

def test_full_house():
    boat_cards = [card1, card14, card2, card15, card28, card47, card20]
    result = evaluate(boat_cards)

    assert result[0] == HandRank.FULL_HOUSE
    assert result[1] == [2, 14]

def test_full_house2():
    boat_cards = [card4, card17, card5, card18, card31, card50, card23]
    result = evaluate(boat_cards)

    assert result[0] == HandRank.FULL_HOUSE
    assert result[1] == [5, 4]

def test_no_full_house():
    no_boat_cards = [card6, card11, card7, card34, card51, card16, card31]
    result = evaluate(no_boat_cards)

    assert result != HandRank.FULL_HOUSE

## STRAIGHT FLUSH TESTS

def test_straight_flush():
    wheel_straight_flush_cards = [card1, card2, card3, card4, card5, card31, card43]
    result = evaluate(wheel_straight_flush_cards)

    assert result[0] == HandRank.STRAIGHT_FLUSH
    assert result[1] == [5, 4, 3, 2, 1]

def test_straight_flush2():
    straight_flush_cards = [card6, card7, card8, card9, card10, card31, card43]
    result = evaluate(straight_flush_cards)

    assert result[0] == HandRank.STRAIGHT_FLUSH
    assert result[1] == [10, 9, 8, 7, 6]

def test_no_straight_flush():
    no_straight_flush_cards = [card8, card2, card13, card4, card5, card31, card43]
    result = evaluate(no_straight_flush_cards)

    assert result != HandRank.STRAIGHT_FLUSH

## TRIPS TESTS

def test_trips():
    trips_cards = [card8, card21, card34, card1, card2, card43, card44]
    result = evaluate(trips_cards)

    assert result[0] == HandRank.THREE_OF_A_KIND
    assert result[1] == [8, 14, 5]

def test_trips2():
    trips_cards = [card7, card20, card29, card33, card2, card43, card44]
    result = evaluate(trips_cards)

    assert result[0] == HandRank.THREE_OF_A_KIND
    assert result[1] == [7, 5, 4]

def test_no_trips():
    no_trip_cards = [card6, card20, card29, card33, card2, card43, card44]
    result = evaluate(no_trip_cards)

    assert result != HandRank.THREE_OF_A_KIND

## TWO PAIR TESTS

def test_two_pair():
    two_pair_cards = [card1, card14, card2, card15, card52, card51, card50]
    result = evaluate(two_pair_cards)

    assert result[0] == HandRank.TWO_PAIR
    assert result[1] == [14, 2, 13]

def test_two_pair2():
    two_pair_cards = [card3, card16, card6, card19, card52, card51, card50]
    result = evaluate(two_pair_cards)

    assert result[0] == HandRank.TWO_PAIR
    assert result[1] == [6, 3, 13]

def test_no_two_pair():
    two_pair_cards = [card16, card14, card2, card15, card52, card51, card50]
    result = evaluate(two_pair_cards)

    assert result != HandRank.TWO_PAIR

## ONE PAIR TESTS
def test_one_pair():
    one_pair_cards = [card13, card26, card27, card50, card5, card9, card34]
    result = evaluate(one_pair_cards)

    assert result[0] == HandRank.ONE_PAIR
    assert result[1] == [13, 14, 11, 9]

def test_one_pair2():
    one_pair_cards = [card15, card28, card27, card50, card5, card9, card34]
    result = evaluate(one_pair_cards)

    assert result[0] == HandRank.ONE_PAIR
    assert result[1] == [2, 14, 11, 9]

def test_no_one_pair():
    one_pair_cards = [card13, card29, card27, card50, card5, card9, card34]
    result = evaluate(one_pair_cards)

    assert result != HandRank.ONE_PAIR

## HIGH CARD TESTS
def test_high_card():
    high_card_cards = [card14, card30, card28, card51, card6, card10, card35]
    result = evaluate(high_card_cards)

    assert result[0] == HandRank.HIGH_CARD
    assert result[1] == [14, 12, 10, 9, 6]

def test_no_high_card():
    high_card_cards = [card19, card30, card28, card51, card6, card10, card35]
    result = evaluate(high_card_cards)

    assert result != HandRank.HIGH_CARD
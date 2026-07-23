from poker.card import Card, Rank, Suit

Ace_Of_Spades = Card(Rank.ACE, Suit.SPADE)
Five_Of_Diamonds = Card(Rank.FIVE, Suit.DIAMOND)

def test_string_to_card():
    assert str(Ace_Of_Spades) == "As"
    assert str(Five_Of_Diamonds) == "5d"

def comparison():
    assert Ace_Of_Spades.rank > Five_Of_Diamonds.rank

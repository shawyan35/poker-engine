from poker.card import Card, Rank, Suit
from poker.montecarlo import simulate


def parse_card(card_str: str) -> Card:

    RANKS = {"2" : Rank.TWO, "3" : Rank.THREE, "4" : Rank.FOUR, "5" : Rank.FIVE, "6" : Rank.SIX, "7" : Rank.SEVEN, "8" : Rank.EIGHT, "9" : Rank.NINE, "10" : Rank.TEN, "J" : Rank.JACK, "Q" : Rank.QUEEN, "K" : Rank.KING, "A" : Rank.ACE}
    SUITS = {"h" : Suit.HEART, "d" : Suit.DIAMOND, "s" : Suit.SPADE, "c" : Suit.CLUB}

    try:
        rank = RANKS[card_str[:-1]]
        suit = SUITS[card_str[-1]]
        
        return Card(rank, suit)

    except (IndexError, KeyError):
        raise ValueError(f"Invalid Card {card_str}")

def parse_hand(hand_str: str) -> list[Card]:
    cards = []
    current_card = ""
    
    for char in hand_str:
        current_card += char
        if char.islower():
            cards.append(parse_card(current_card))
            current_card = ""

    return cards

def main():
    
    hand1 = input("Enter your hand. e.g. Ah5c -> Ace of Hearts, Five of Clubs: ")
    hand1 = parse_hand(hand1)

    hand2 = input("Enter your hand. e.g. 10sJd -> Ten of Spades, Jack of Diamonds: ")
    hand2 = parse_hand(hand2)

    board = input("Enter the board. If preflop, do nothing and press enter: ")
    board = parse_hand(board)

    num_sims = input("Enter number of simulations (default 10000): ")
    num_sims = int(num_sims) if num_sims else 10000 

    result = simulate(hand1, hand2, board, num_sims)
    print(f"Hand 1: {round(result[0], 2)}%")
    print(f"Hand 2: {round(result[1], 2)}%")
    print(f"Ties:   {round(result[2], 2)}%")

if __name__ == "__main__": main()
from poker.deck import Deck
from poker.card import Card
from poker.evaluator import evaluate

def simulate(hand1: list[Card], hand2: list[Card], board: list[Card], num_simulations: int) -> tuple[float, float, float]:
    """Runs simulations to determine the equity of each players hands in specific scenarios"""

    known_cards = hand1 + hand2 + board
    player1_wins = 0
    player2_wins = 0
    draws = 0
    master_deck = Deck()
    base_cards = [card for card in master_deck.cards if card not in known_cards]
    cards_needed = 5 - len(board)

    for i in range(num_simulations):

        master_deck.cards = base_cards[:]
        master_deck.shuffle()

        newly_dealt_cards = master_deck.deal(cards_needed)

        player1_cards = hand1 + board + newly_dealt_cards
        player2_cards = hand2 + board + newly_dealt_cards

        print(player1_cards)

        result1 = evaluate(player1_cards)
        result2 = evaluate(player2_cards)

        if result1 > result2:
            player1_wins += 1

        elif result2 > result1:
            player2_wins += 1
        else:
            draws += 1
    
    multiplier = 100 / num_simulations
    return player1_wins * multiplier, player2_wins * multiplier, draws * multiplier






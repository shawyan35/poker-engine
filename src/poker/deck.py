from poker.card import Card, Rank, Suit
import random

class Deck:
    def __init__(self):
        self.cards = [Card(r, s) for r in Rank for s in Suit]

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)
    
    def deal(self, n):
        if n > len(self.cards):
            raise ValueError("Not enough cards left in the deck")
            
        return [self.cards.pop() for _ in range(n)]



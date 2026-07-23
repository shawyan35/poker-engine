from enum import Enum
from enum import IntEnum
from dataclasses import dataclass


class Suit(Enum):
    SPADE = "s"
    HEART = "h"
    DIAMOND = "d"
    CLUB = "c"

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@dataclass(frozen=True)
class Card:
    rank: Rank
    suit: Suit
    
    RANK_SYMBOLS = {
        10: "T",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",

    }

    def __str__(self) -> str:
        rank_str = self.RANK_SYMBOLS.get(self.rank.value, str(self.rank.value))
        suit_str = self.suit.value
        return f"{rank_str}{suit_str}"

    def __repr__(self) -> str:
        return self.__str__()
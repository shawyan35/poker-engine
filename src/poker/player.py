from dataclasses import dataclass, field

@dataclass
class Player:
    stack: int
    is_active: bool = True
    bet_this_round: int = 0
    is_all_in: bool = False
    hole_cards: list[str] = field(default_factory=list)

from dataclasses import dataclass
from enum import Enum
from typing import Callable, List

class Play(Enum):
    defect = 'defect'
    cooperate = 'cooperate'

@dataclass
class PlayerRound:
    you: Play
    them: Play

@dataclass
class Round:
    play1: Play
    play2: Play
    player1_score: int
    player2_score: int



@dataclass
class TournamentOutput:
    player1: str
    player2: str
    player1_score: int
    player2_score: int
    player1_history: List[PlayerRound]
    player2_history: List[PlayerRound]
    history: List[Round]



PlayerRoundHistory = List[PlayerRound]
RoundHistory = List[Round]

Player = Callable[[PlayerRoundHistory], Play]
import random
from custom_types import Play, PlayerRoundHistory


def random_player(
        prev: PlayerRoundHistory
    ):
    if random.random() < 0.5:
        return Play.cooperate
    
    return Play.defect
from custom_types import Play, PlayerRoundHistory


def always_defect(
        prev: PlayerRoundHistory
    ) -> Play:
    return Play.defect


def always_cooperate(
        prev: PlayerRoundHistory
    ) -> Play:
    return Play.cooperate
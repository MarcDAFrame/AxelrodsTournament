from custom_types import Play, PlayerRoundHistory


def tit4tat(
        prev: PlayerRoundHistory
    ) -> Play:
    if len(prev) == 0:
        return Play.cooperate
    if prev[-1].them == Play.defect:
        return Play.defect
    return Play.cooperate
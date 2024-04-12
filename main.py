import random
from typing import List
import pandas as pd

from custom_types import Player, Round, Play, PlayerRound, PlayerRoundHistory, TournamentOutput


def apply_noise(play, should_apply_noise=bool):
    """
    helper function for applying the noise
    """
    if should_apply_noise:
        if play == Play.cooperate:
            return Play.defect
        return Play.cooperate
    return play



def run_tournament(
        player1: Player,
        player2: Player,
        n=200,
        noise=0,
        cooperate_score=3,
        defect_score=5,
        stalemate_score=1,
        lose_score=0,
    ) -> TournamentOutput:
    """
    
    """

    history: PlayerRoundHistory = []
    player1_history: PlayerRoundHistory = []
    player2_history: PlayerRoundHistory = []
    player1_score = 0
    player2_score = 0
    for i in range(n):
        play1 = player1(player1_history)
        play2 = player2(player2_history)

        should_apply_noise = random.random() < noise


        # interestingly, the %autoreload breaks the Enum comparison here because it reinstantiates the Enum in one file but not another so they have different instances
        if play1 == Play.cooperate and play2 == Play.cooperate:
            player1_score += cooperate_score
            player2_score += cooperate_score
        
        if play1 == Play.cooperate and play2 == Play.defect:
            player1_score += lose_score
            player2_score += defect_score
        
        if play1 == Play.defect and play2 == Play.cooperate:
            player1_score += defect_score
            player2_score += lose_score
        
        if play1 == Play.defect and play2 == Play.defect:
            player1_score += stalemate_score
            player2_score += stalemate_score

        history.append(
            Round(
                play1=play1,
                play2=play2,
                player1_score=player1_score, # was thinking of including this but then realized you could figure out when there was noise by looking at the score
                player2_score=player2_score,
            )
        )
        player1_history.append(
            PlayerRound(
                you=play1,
                them=apply_noise(play2, should_apply_noise=should_apply_noise),
                # you_score=player1_score,
                # them_score=player2_score,
            )
        )
        player2_history.append(
            PlayerRound(
                you=play2,
                them=apply_noise(play1, should_apply_noise=should_apply_noise),
                # you_score=player2_score,
                # them_score=player1_score,
            )
        )

    return TournamentOutput(
        player1=player1.__name__,
        player2=player2.__name__,
        player1_score=player1_score,
        player2_score=player2_score,
        player1_history=player1_history,
        player2_history=player2_history,
        history=history,
    )

def run(
    players=None,
    n=200,
    n_deviation=1,
    noise=0,
):
    """
    players : Optional[List[Player]] : players to be run in the tournament
    n : int : number of simulations to run
    n_deviation : int : random amount to deviate from the number of simulations
    noise : float : 0 to 1 what percent of rounds to apply noise to
    """
    n_rounds = n + random.randint(-n_deviation, n_deviation)
    tournament_outputs: List[TournamentOutput] = []
    
    for i, player1 in enumerate(players):
        for player2 in players[i+1:]:
            print("RUNNING", player1.__name__, "vs", player2.__name__)
            # if player1 == player2:
            #     continue

            tournament_output = run_tournament(
                player1=player1,
                player2=player2,
                n=n_rounds,
                noise=noise
            )
            tournament_outputs.append(
                tournament_output
            )

    rounds_data = []
    for output in tournament_outputs:
        for idx, round in enumerate(output.history):
                # print(round)
                round_data = {
                    'player1' : output.player1,
                    'player2' : output.player2,
                    'tournament_id': id(output),  # Unique identifier for the tournament
                    'round_number': idx + 1,
                    # 'player1_history_you': output.player1_history[idx].you.value,
                    'player1_history_them': output.player1_history[idx].them.value,
                    # 'player2_history_you': output.player2_history[idx].you.value,
                    'player2_history_them': output.player2_history[idx].them.value,
                    'player1_play' : round.play1.value,
                    'player2_play' : round.play2.value,
                    'player1_score': round.player1_score,
                    'player2_score': round.player2_score
                }
                rounds_data.append(round_data)


    tournament_data = []
    for tournament in tournament_outputs:
        tournament_data.append({
            'player1_score': tournament.player1_score,
            'player2_score': tournament.player2_score,
            'player1' : tournament.player1,
            'player2' : tournament.player2,
        })

    rounds_df = pd.DataFrame(rounds_data)
    tournament_df = pd.DataFrame(tournament_data)

    return rounds_df, tournament_df
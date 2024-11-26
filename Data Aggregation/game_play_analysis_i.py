# Game Play Analysis I
# Write a solution to find the first login date for each player.
# Solution for the 'Game Play Analysis I' problem.
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].agg(min).reset_index().rename(columns = {'event_date': 'first_login'})

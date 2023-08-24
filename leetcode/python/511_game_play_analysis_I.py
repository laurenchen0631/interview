import pandas as pd

# SELECT player_id, MIN(event_date) AS first_login
# FROM Activity
# GROUP BY player_id
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id')['event_date'].min().reset_index()
    return activity.rename(columns={'event_date': 'first_login'})
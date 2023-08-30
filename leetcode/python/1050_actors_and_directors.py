import pandas as pd

# SELECT actor_id, director_id
# FROM ActorDirector
# GROUP BY actor_id, director_id
# HAVING COUNT(*) >= 3
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    group = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    return group[group['count'] >= 3][['actor_id', 'director_id']]
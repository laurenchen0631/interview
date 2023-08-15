# SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' 
# FROM Scores
# ORDER BY score DESC

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values('score', ascending=False)
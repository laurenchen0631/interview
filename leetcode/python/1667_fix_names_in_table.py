
import pandas as pd


# SELECT
#   user_id,
#   CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
# FROM Users
# ORDER BY user_id;
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users.copy()
    df = df.assign(
        name=df.name.str[0].str.upper() + df.name.str[1:].str.lower()
    )
    df.sort_values('user_id', inplace=True)
    return df
    
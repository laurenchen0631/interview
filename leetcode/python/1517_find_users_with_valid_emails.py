
import pandas as pd

# SELECT *
# FROM Users
# WHERE mail REGEXP '^[a-zA-Z]+[a-zA-Z0-9._-]*@leetcode\\.com$'
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['mail'].str.match(r'^[a-zA-Z]+[a-zA-Z0-9._-]*@leetcode\.com$')]
    return df
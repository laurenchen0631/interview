# DELETE p1
# FROM Person p1, Person p2
# WHERE p1.email = p2.email AND p1.id > p2.id;

import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby('email')['id'].transform(min)
    removed = person[person['id'] != min_id]
    person.drop(removed.index, inplace=True)
    
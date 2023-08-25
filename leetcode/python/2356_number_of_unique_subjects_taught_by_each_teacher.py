import pandas as pd

# SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
# FROM Teacher
# GROUP BY teacher_id;
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(['teacher_id'])["subject_id"].nunique().reset_index(name="cnt")
    return df
import pandas as pd

# SELECT class
# FROM Courses
# GROUP BY class
# HAVING COUNT(*) >= 5;
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class').filter(lambda x: len(x) >= 5)
    
    return courses[['class']].drop_duplicates()
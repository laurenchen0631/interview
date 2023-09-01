import pandas as pd

# SELECT 
#     s.student_id,
#     s.student_name, 
#     sub.subject_name,
#     IFNULL(grouped.attended_exams, 0) AS attended_exams
# FROM Students s
# CROSS JOIN Subjects sub
# LEFT JOIN (
#     SELECT student_id, subject_name, COUNT(*) AS attended_exams
#     FROM Examinations
#     GROUP BY student_id, subject_name
# ) grouped
#     ON s.student_id = grouped.student_id AND sub.subject_name = grouped.subject_name
# ORDER BY s.student_id, sub.subject_name;
def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Group by id and subject and count the number of exams.
    grouped = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
    # Get all combinations of (id, subject) 
    all_id_subjects = pd.merge(students, subjects, how='cross')
    
    # Left join to retain all combinations.
    id_subjects_count = pd.merge(all_id_subjects, grouped, on=['student_id', 'subject_name'], how='left')
    
    # Data cleaning.
    id_subjects_count['attended_exams'] = id_subjects_count['attended_exams'].fillna(0).astype(int)
    id_subjects_count.sort_values(['student_id', 'subject_name'], inplace=True)
    
    return id_subjects_count[['student_id', 'student_name', 'subject_name', 'attended_exams']]
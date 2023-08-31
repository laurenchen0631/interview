import pandas as pd

# SELECT unique_id, name
# FROM Employees
#     LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, employee_uni, how='left', left_on='id', right_on='id')
    return merged[['unique_id', 'name']]
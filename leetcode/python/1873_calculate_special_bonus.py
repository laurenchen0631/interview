import pandas as pd

# SELECT 
#   employee_id, 
#   salary * IF(MOD(employee_id, 2) = 1 AND name NOT LIKE 'm%', 1, 0) AS `bonus`
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] * (1 if row['employee_id'] % 2 == 1 and not row['name'].startswith('M') else 0),
        axis=1
    )
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])
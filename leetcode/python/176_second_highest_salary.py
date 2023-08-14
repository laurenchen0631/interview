import pandas as pd

# SELECT * 
# FROM (
#   SELECT DISTINCT salary
#   FROM Employee
#   ORDER BY salary DESC
#   LIMIT 1 OFFSET 1
# ) AS SecondHighestSalary

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary'])
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    employee = employee.sort_values(by=['salary'], ascending=False)
    employee = employee.head(2).tail(1)
    employee.rename(columns={'salary': 'SecondHighestSalary'}, inplace=True)
    return employee[['SecondHighestSalary']]
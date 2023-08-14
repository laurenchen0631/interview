import pandas as pd

# SELECT e.name as NAME, e.salary as SALARY, d.name as DEPARTMENT
# FROM Employee e
#     JOIN Department d ON e.departmentId = d.id
# WHERE (e.departmentId, e.salary) IN (
#     SELECT departmentId, MAX(salary)
#     FROM Employee
#     GROUP BY departmentId
# )

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id')
    df.rename(columns={'name_x': 'Employee', 'salary': 'Salary', 'name_y': 'Department'}, inplace=True)
    
    max_salary = df.groupby(['Department'])['Salary'].transform(max)
    df = df[df['Salary'] == max_salary]
    return df[['Department', 'Employee', 'Salary']]
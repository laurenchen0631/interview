import pandas as pd

# SELECT 
#   event_day as day,
#   emp_id,
#   sum(out_time - in_time) as total_time
# FROM Employees
# GROUP BY event_day, emp_id
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day', 'emp_id']).sum().reset_index()
    employees.rename(columns={'event_day': 'day'}, inplace=True)
    return employees[['day', 'emp_id', 'total_time']]
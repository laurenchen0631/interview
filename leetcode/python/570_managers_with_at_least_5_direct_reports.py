import pandas as pd

# SELECT name
# FROM Employee
# WHERE id IN (
#    SELECT managerId
#    FROM Employee
#    GROUP BY managerId
#    HAVING COUNT(id) >= 5
# )
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby('managerId').count()
    managers = managers[managers['id'] >= 5]
    
    return employee[employee['id'].isin(managers.index)][['name']]
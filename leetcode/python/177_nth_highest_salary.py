# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
#   SET N = N - 1;
#   RETURN (
#     SELECT DISTINCT salary
#     FROM Employee
#     ORDER BY salary DESC
#     LIMIT 1 OFFSET N 
#   );
# END

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    N = N - 1
    df = employee.sort_values(by='salary', ascending=False).iloc[N:N+1]
    return df

SELECT
    'Low Salary' AS 'Category',
    SUM(CASE WHEN income < 20000 THEN 1 ELSE 0 END) AS 'accounts_count'
FROM Accounts

UNION

SELECT
    'Average Salary' AS 'Category',
    SUM(IF(income >= 20000 AND income <= 50000, 1, 0)) AS 'accounts_count'
FROM Accounts

UNION

SELECT
    'High Salary' AS 'Category',
    SUM(IF(income > 50000, 1, 0)) AS 'accounts_count'
FROM Accounts

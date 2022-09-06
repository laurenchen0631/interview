import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="leetcode",
    user=os.environ["PS_USER"],
    password=os.environ["PS_PASS"])

with conn.cursor() as cur:
    cur.execute("Create table If Not Exists Employee (id int, salary int)")
    cur.execute("Truncate table Employee")
    cur.execute("insert into Employee (id, salary) values ('1', '100')")
    cur.execute("insert into Employee (id, salary) values ('2', '200')")
    cur.execute("insert into Employee (id, salary) values ('3', '300')")

conn.commit()
   
with conn.cursor() as cur:
    cur.execute("""
        SELECT * 
        FROM (
            SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET 1
        ) AS SecondHighestSalary
    """)
    row = cur.fetchone()
    print(cur.description)
    print(row)

conn.close()


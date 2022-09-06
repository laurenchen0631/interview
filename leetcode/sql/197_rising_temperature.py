import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="leetcode",
    user=os.environ["PS_USER"],
    password=os.environ["PS_PASS"])

with conn.cursor() as cur:
    cur.execute("Create table If Not Exists Weather (id int, recordDate date, temperature int)")
    cur.execute("Truncate table Weather")
    cur.execute("insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')")
    cur.execute("insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')")
    cur.execute("insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')")
    cur.execute("insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')")

conn.commit()
   
with conn.cursor() as cur:
    cur.execute("""
        SELECT id
        FROM Weather t
        WHERE NOT Exists (
            SELECT * 
            FROM Weather y
            WHERE DATE_PART('day', t.recordDate::timestamp - y.recordDate::timestamp) = 1
                AND t.temperature > y.temperature
            );
    """)
    row = cur.fetchall()
    print(cur.description)
    for r in row:
        print(r)

conn.close()


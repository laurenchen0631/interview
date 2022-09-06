import math
import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user=os.environ["PS_USER"],
    password=os.environ["PS_PASS"],
)

def create_table():
    with conn.cursor() as cur:
        cur.execute("""
           Create table Accidents (
                "Severity" int,
                "Distance(mi)" decimal(8,2),
                "Start_Time" timestamp,
                "End_Time" timestamp,
                "Start_Lat" decimal(10, 6),
                "Start_Lng" decimal(10, 6),
                "Street" varchar(255),
                "City" varchar(255),
                "Temperature(F)" decimal(8, 1),
                "Junction" boolean,
                "Wind_Speed(mph)" decimal(8, 3),
                "Precipitation(in)" decimal(8, 2),
                "Weather_Condition" varchar(64)
            );
        """)

        cur.execute("""
            COPY Accidents
            FROM 'US_Accidents_Dec21_03.csv'
            DELIMITER ‘,’
            CSV Header;
        """)

        cur.execute("""
            DELETE FROM accidents
            WHERE "Start_Lat" < 32.52 OR "Start_Lat" > 42.00 OR "Start_Lng" < -124.40 OR "Start_Lng" > -114.14;
        """)
        conn.commit()

def find_highest_accidents_hour():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT DATE_PART('hour', "Start_Time") As hour, count(*)
            FROM accidents
            GROUP BY DATE_PART('hour', "Start_Time")
            ORDER BY count(*) DESC
            LIMIT 1;
        """)
        row = cur.fetchone()
        print(row[0])

def find_top3_accident_city():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT "City", COUNT(*) AS count
            FROM accidents
            WHERE DATE_PART('hour', "Start_Time") <= 4 AND DATE_PART('hour', "End_Time") >= 3
            GROUP BY "City"
            ORDER BY count(*) DESC
            LIMIT 3;
        """)
        rows = cur.fetchall()
        res = []
        for r in rows:
            res.append(r[0])
            res.append(str(r[1]))
        print(','.join(res))

def find_high_wind_weather():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT "Weather_Condition", count(*) AS count
            FROM accidents
            WHERE "Wind_Speed(mph)" > 20
            GROUP BY "Weather_Condition"
            ORDER BY count(*) DESC
            LIMIT 1
        """)
        row = cur.fetchone()
        print(row[0])

def count_on_junction_hotday():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) AS count
            FROM accidents
            WHERE "Junction" = true AND "Temperature(F)" > 92;
        """)
        row = cur.fetchone()
        print(row[0])

def avg_precipitation_on_rain():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT AVG("Precipitation(in)") AS avg
            FROM accidents
            WHERE "Precipitation(in)" > 0;
        """)
        row = cur.fetchone()
        print(math.floor(row[0] * 10**3) / 10**3)

# create_table()
find_highest_accidents_hour()
find_top3_accident_city()
find_high_wind_weather()
count_on_junction_hotday()
avg_precipitation_on_rain()


conn.close()
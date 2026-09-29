from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

database_url = os.getenv("cross_string")

with psycopg.connect(database_url) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("Database connected:", cursor.fetchone())
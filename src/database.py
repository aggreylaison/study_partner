from psycopg import connect
import os
from dotenv import load_dotenv

load_dotenv()

db_url=os.getenv("cross_string")

conn=connect(db_url)


conn.close()

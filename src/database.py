from psycopg import connect
import os
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()

db_url=os.getenv("cross_string")

def get_conection():

    conn=connect(db_url)

    return conn

def insert_chunks(conn,content,embedding):
    cur=conn.cursor()

    cur.execute( "INSERT INTO document_chunks (content,embedding) VALUES(%,%)",(content,embedding))

    conn.commit()

    cur.close()

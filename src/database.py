from psycopg import connect
import os
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()

db_url=os.getenv("cross_string")


def get_conection():

    conn=connect(db_url)

    return conn

def insert_chunks(conn,document_id,content,chunk_index,embedding):
    register_vector(conn)
    cur=conn.cursor()

    cur.execute( 
        "INSERT INTO document_chunks (document_id,content,chunk_index,embedding) VALUES(%s,%s,%s,%s)",
        (document_id,content,chunk_index,embedding)
        )

    conn.commit()

    cur.close()

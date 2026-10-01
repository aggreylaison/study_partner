import os
import psycopg
from database import get_conection
from user import insert_dummy_user

file_path="/home/aggrey/Projects/ai_agent/ML_DL_Agentic_AI_Notes.pdf"

filename=os.path.basename(file_path)

conn=get_conection()
user_id=insert_dummy_user(conn, "john")

def insert_doc_name(conn,filename,user_id):
    cur=conn.cursor()

    cur.execute("INSERT INTO documents(filename,user_id) VALUES(%s,%s)",(filename,user_id))

    conn.commit()

    cur.close()


insert_doc_name(conn,filename,user_id)



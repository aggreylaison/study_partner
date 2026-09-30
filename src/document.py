import os
import psycopg
from database import get_conection


file_path="/home/aggrey/Projects/ai_agent/ML_DL_Agentic_AI_Notes.pdf"

filename=os.path.basename(file_path)

conn=get_conection()

def insert_doc_name(conn,filename):
    cur=conn.cursor()

    cur.execute("INSERT INTO documents(filename) VALUES(%s)",(filename,))

    conn.commit()

    cur.close()


insert_doc_name(conn,filename)



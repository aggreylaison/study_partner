import os
import psycopg
from database import get_conection
from user import get_user_id

file_path="/home/aggrey/Projects/ai_agent/ML_DL_Agentic_AI_Notes.pdf"

filename=os.path.basename(file_path)

conn=get_conection()
user_id=get_user_id(conn, "john")

def insert_doc_name(conn,filename,user_id):
    cur=conn.cursor()

    cur.execute("""INSERT INTO documents(filename,user_id) VALUES(%s,%s) RETURNING id""",(filename,user_id))

    document_id=cur.fetchone()[0]

    conn.commit()

    return document_id


document_id=insert_doc_name(conn,filename,user_id)
print(document_id)



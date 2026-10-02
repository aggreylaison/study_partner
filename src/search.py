import psycopg
from database import get_conection
from embedding import get_embedding
from pgvector.psycopg import register_vector


def search(conn,query_embedded,top_k=5):
    register_vector(conn)
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT content

            FROM document_chunks

            ORDER BY embedding <=> %s

            LIMIT %s

            """,
            (query_embedded,top_k)

        )

        result=cur.fetchall()


    return result


query="typical ML workflow"

query_embedded=get_embedding(query)

conn=get_conection()

simiral=search(conn,query_embedded,top_k=5)

print(simiral)

conn.close()
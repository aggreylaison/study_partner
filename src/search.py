import psycopg
from src.database import get_conection
from src.embedding import get_embedding
from pgvector.psycopg import register_vector


def search(conn,query_embedded,top_k=3):
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

simiral=search(conn,query_embedded,top_k=3)

context="\n\n".join(chunk[0] for chunk in simiral)

print(context)

conn.close()
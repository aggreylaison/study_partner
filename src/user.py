from database import get_conection

conn=get_conection()

def insert_dummy_user(conn, username):

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (username) VALUES (%s) RETURNING id",
            (username,)
        )
        user_id = cur.fetchone()[0]

    conn.commit()
    return user_id

def get_user_id(conn, username):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id FROM users WHERE username = %s",(username,)
        )
        result=cur.fetchone()

        return result[0] if result else None

    

user_id = get_user_id(conn, "john")
print(user_id)
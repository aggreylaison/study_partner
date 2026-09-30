from database import get_conection


def get_users_columns(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = 'users'
            ORDER BY ordinal_position
            """
        )
        return [row[0] for row in cur.fetchall()]


def insert_dummy_user(conn, username):
    columns = get_users_columns(conn)
    lower_columns = {column.lower(): column for column in columns}

    if 'username' in lower_columns:
        column_name = lower_columns['username']
        sql = f"INSERT INTO users ({column_name}) VALUES (%s)"
        params = (username,)
    elif 'name' in lower_columns:
        column_name = lower_columns['name']
        sql = f"INSERT INTO users ({column_name}) VALUES (%s)"
        params = (username,)
    else:
        sql = "INSERT INTO users (username) VALUES (%s)"
        params = (username,)

    with conn.cursor() as cur:
        cur.execute(sql, params)

    conn.commit()
    print(f"Inserted dummy user: {username}")


if __name__ == "__main__":
    conn = get_conection()
    try:
        insert_dummy_user(conn, "aggrey")
    finally:
        conn.close()

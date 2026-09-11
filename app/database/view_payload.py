from app.database.database import get_connection

def view_payload():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    SELECT * FROM payloads
    """

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    finally:
        cursor.close()
        connection.close()


view_payload()
    
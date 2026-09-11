from app.database.database import get_connection

def createPayloadTable():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payloads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            record VARCHAR(80),
            ingestion_id VARCHAR(80),
            file VARCHAR(80),
            status VARCHAR(100),
            total VARCHAR(10),
            errors VARCHAR(10),
            ingestion_time DATETIME,
            elapsed_time VARCHAR(10),
            in_svc VARCHAR(100),
            out_svc VARCHAR(100)
        )
    """)
    
    connection.commit()
    print("Payload table created.")

    cursor.close()
    connection.close()
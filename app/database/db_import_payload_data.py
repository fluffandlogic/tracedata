
import csv
import os
import mysql.connector
from dotenv import load_dotenv
from app.database.database import get_connection
from datetime import datetime, timezone

load_dotenv()

def import_csv(file_path):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO payloads (
            record,
            ingestion_id,
            file,
            status,
            total,
            errors,
            ingestion_time,
            elapsed_time,
            in_svc,
            out_svc
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with open(file_path,mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            # for row in reader:
            #     print(row)

            for row in reader:
                ingestion_time = datetime.strptime(
                    row["ingestion_time"].strip(),
                    "%m/%d/%Y %I:%M %p"
                ).replace(tzinfo=timezone.utc)

                cursor.execute(
                    sql,
                    (
                        row["record"],
                        row["ingestion_id"],
                        row["file"],
                        row["status"],
                        row["total"],
                        row["errors"],
                        ingestion_time,
                        row["elapsed_time"],
                        row["in_svc"],
                        row["out_svc"],
                    )
                )
    
            connection.commit()
            print("CSV imported successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Import failed: {error}")

    finally:
        cursor.close()
        connection.close()

import_csv("payloads.csv")
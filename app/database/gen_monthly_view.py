import random
import datetime
import math
from database import get_connection

entities = [ "applicationReceiptAcknowledgement", "asset", "assetActivity", "assetAssignment",
    "attributeDefinition", "attributeGroup", "autoApprovalException", "autoApprovalRule", 
    "batchNotification", "billOfMaterial", "bulkNotification", "calendar", "casePackTemplate", 
    "commodity", "competitor", "crossDockOrder", "customsConsignment", "customerOrderConsumptionPlan"
    ]

operations = [ "ingestion", "validation", "transformation", "interop", "distribution", "egress" ]

statuses = ["Successful", "Successful w/ Error(s)", "Partial Load w/o Error(s)", "Processing", 
          "Pass with Warning", "Stop and Report", "Failed"]

monthlyViewData = []
today = datetime.datetime.now()

for entity in entities:
    # Create enough data for the previous month
    # dates should be formatted as YYYY-MM-DD HH:MM:SS to make them SQL-friendly

    for i in range(1,31):
        month = str(today.month).zfill(2)
        date = str(i).zfill(2)
        hours = '{:.0f}'.format(random.uniform(0,23)).zfill(2)
        minutes = '{:.0f}'.format(random.uniform(0,59)).zfill(2)
        seconds = '{:.0f}'.format(random.uniform(0,59)).zfill(2)

        start_date = f"{today.year}-{month}-{date} {hours}:{minutes}:{seconds}"

        if random.random() > 0.3:
            success = round(random.uniform(85,100),2)
        else:
            success = round(random.uniform(50,100),2)
        fail = round(100 - float(success),2)
        # entity = entities[int(random.uniform(0,len(entities)))]
        operation = operations[int(random.uniform(0,len(operations)))]
        status = statuses[int(random.uniform(0,len(statuses)))]
        data = (entity, success, fail, operation, status, start_date)
        monthlyViewData.append(data)

    # for data in monthlyViewData:
    #     print(f"{data}")

try:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monthly_view (
            id INT AUTO_INCREMENT PRIMARY KEY,
            entity VARCHAR(100),
            success DECIMAL(8,4),
            fail DECIMAL(8,4),
            operation VARCHAR(100),
            status VARCHAR(100),
            start_date DATETIME
        )
    """)
    
    connection.commit()
    print("Monthly View table created.")

    sql = """
        INSERT INTO monthly_view (
            entity,
            success,
            fail,
            operation,
            status,
            start_date
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for row in monthlyViewData:
        cursor.execute(
            sql,
            (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
            )
        )

    connection.commit()
    print("Data imported into monthly_view successfully.")

except Exception as error:
    connection.rollback()
    print(f"Import failed: {error}")

finally:
    cursor.close()
    connection.close()
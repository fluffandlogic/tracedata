from collections import defaultdict
from database.database import get_connection

def calendarData():

    entities = []
    operations = []
    statuses = []
    monthlyData = []

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT DISTINCT entity FROM monthly_view
    """)
    rows = cursor.fetchall()    
    for row in rows:
        entities.append(row[0])

    cursor.execute("""
        SELECT DISTINCT operation FROM monthly_view
    """)
    rows = cursor.fetchall()    
    for row in rows:
        operations.append(row[0])
    

    cursor.execute("""
        SELECT DISTINCT status FROM monthly_view
    """)
    rows = cursor.fetchall()    
    for row in rows:
        statuses.append(row[0])

    cursor.execute("""
        SELECT * FROM monthly_view
    """)
    rows = cursor.fetchall()    
    for row in rows:
        monthlyData.append( {
            "id": row[0],
            "entity": row[1],
            "success": float(row[2]),
            "failure": float(row[3]),
            "operation": row[4],
            "status": row[5],
            "date": row[6]
        })

    cursor.close()
    connection.close()

    data_by_entity = defaultdict(list)

    for row in monthlyData:
        data_by_entity[row["entity"]].append(row)

    return data_by_entity

# for entity, row in calendar().items():
#     print(f"Entity: {entity}")
#     for col in row:
#         print(f" {col['operation']} {col['status']} {col['success']}% {col['date']}")
#     print("\n")
   
# calendar()


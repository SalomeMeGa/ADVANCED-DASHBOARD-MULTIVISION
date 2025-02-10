import mysql.connector
from src.config import MYSQL_CONFIG

def connect_to_mysql():
    """Establecer conexiòn con MySQL"""

    conn = mysql.connector.connect(**MYSQL_CONFIG)
    return conn


if __name__ == "__main__":
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)
    conn.close()


    
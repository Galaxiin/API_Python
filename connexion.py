import pymysql
import pymysql.cursors

class conn:
    def create_conn():
        # Connection a la base de donnee
        conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'your_username',
            password = 'your_password',
            database = 'your_database_name'
        )

        # Create a cursor object
        cursor = conn.cursor()
        return cursor

    def close_conn(cursor: create_conn()):
        # Close the cursor and connection objects
        cursor.close()
        conn.close()
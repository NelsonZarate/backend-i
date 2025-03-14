import sqlite3
from contextlib import contextmanager


@contextmanager
def create_table_using_query():
    print("\nUsing context Manager generator")
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        yield cursor
        print('DB Init')
        query = """
            CREATE TABLE Users (
                User_ID data_type PRIMARY KEY,
                User data_type NOT NULL,
                email data_type NOT NULL UNIQUE,
                password data_type NOT NULL
            );
            
        """
        cursor.execute(query)
        result = cursor.fetchall()
        result
        print(f'Table: {result}')
    except sqlite3.Error as error:
        print('Error occurred - ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')
            
# Usage example:
if __name__ == "__main__":
        with create_table_using_query() as q:
            print("Table created")
  


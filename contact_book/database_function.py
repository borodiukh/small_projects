import sqlite3


# return a Connection object which represents an SQLite database
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    connection_object = None
    try:
        connection_object = sqlite3.connect(db_file)
        # print(sqlite3.version)
    except sqlite3.Error as error_message:
        print(error_message)
    finally:
        return connection_object


def create_table(connection_object, create_table_sql):
    try:
        cursor_object = connection_object.cursor()
        cursor_object.execute(create_table_sql)
    except sqlite3.Error as error_message:
        print(error_message)


def main():
    database = 'contact_book.db'

    sql_create_user = """CREATE TABLE IF NOT EXISTS User (
                        name TEXT NOT NULL,
                        phone_number INTEGER PRIMARY KEY,
                        address TEXT,
                        email_address TEXT);
                        """

    sql_create_country_code = """CREATE TABLE IF NOT EXISTS Country_codes (
                                 country_name TEXT NOT NULL,
                                 code INTEGER NOT NULL);"""

    # create a database connection
    connection_object = create_connection(database)

    # create tables
    if connection_object is not None:
        # create user table
        create_table(connection_object, sql_create_user)
        # create_table(connection_object, sql_create_country_code)
    else:
        print("Error! cannot create the database connection.")


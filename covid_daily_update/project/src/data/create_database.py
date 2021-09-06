# The "create_database_and_tables" function creates the database and its two tables if they do not exist.


def create_database_and_tables(cursor):
    """
    Summary: Creates a database and the "covid_states" and "covid_brazil" of them do not exist.

    Args:
      : cursor (sqlite3 cursor): Cursor of the connection with the database
    """

    import sqlite3

    #! Creates the "covid_states" and "covid_brazil" tables if they do not exist.
    cursor.execute("""CREATE TABLE IF NOT EXISTS covid_states (
                            state VARCHAR(100),
                            date DATE,
                            confirmed_accumulated INTEGER,
                            confirmated_difference INTEGER,
                            deaths_accumulated INTEGER,
                            deaths_difference INTEGER,
                            last_update TIMESTAMP)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS covid_brazil (
                            date DATE,
                            confirmed_accumulated INTEGER,
                            confirmated_difference INTEGER,
                            deaths_accumulated INTEGER,
                            deaths_difference INTEGER,
                            last_update TIMESTAMP)
        """)

    return None

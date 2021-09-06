import sys
import sqlite3

# Add "src" to folders library path
sys.path.append("/opt/airflow/project/src")
from data.populate_database import add_data_in_covid_states_table, add_data_in_brazil_covid_table
from data.create_database import create_database_and_tables

# Path to the database file
PATH = "/opt/airflow/project/data/database/database.db"

# Create connection and cursor with the database
connection = sqlite3.connect(PATH)  # Connect with database or create it
cursor = connection.cursor()

# Execute functions
create_database_and_tables(cursor=cursor)

add_data_in_covid_states_table(cursor=cursor)

add_data_in_brazil_covid_table(cursor=cursor)

connection.commit()  # Commit changes
connection.close()  # Close connection

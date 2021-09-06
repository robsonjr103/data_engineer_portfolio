import sys
# Add "src" to folders library path
sys.path.append("/opt/airflow/project/src")
from data.create_database import create_database_and_tables
from data.populate_database import add_data_in_covid_states_table, add_data_in_brazil_covid_table

# Path to the database file
PATH = "/opt/airflow/project/data/database/database.db"

create_database_and_tables(path=PATH)

add_data_in_covid_states_table(path=PATH)

add_data_in_brazil_covid_table(path=PATH)

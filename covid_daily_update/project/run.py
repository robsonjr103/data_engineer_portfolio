import sys
# Add "src" to folders library path
sys.path.append("/opt/airflow/project/src")
from data.create_database import create_database_and_tables

# Path to the "project" folder
PATH = "/opt/airflow/project"

create_database_and_tables(path=PATH)


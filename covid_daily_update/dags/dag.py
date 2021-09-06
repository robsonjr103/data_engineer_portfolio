import sys
import sqlite3
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow import DAG

# Add src to library path
sys.path.append("/opt/airflow/project/src")
from data.update_data import update_data_covid_brazil, update_data_covid_states
from data.create_database import create_database_and_tables


# Path to the database file
PATH = "/opt/airflow/project/data/database/database.db"

# Create connection and cursor with the database
connection = sqlite3.connect(PATH)
cursor = connection.cursor()


# Function that commit changes and close connection
def commit_and_close_connection(connection, cursor):
    connection.commit()  # Commit changes
    connection.close()  # Close connection
    
    return None 
    
    
with DAG(dag_id="daily_update_covid_tables",
         start_date=datetime(2021, 9, 4),
         schedule_interval="1 13 * * *",
         catchup=False
         ) as dag:

    # Task that performs the function that creates the database and its tables if they do not exist
    create_database = PythonOperator(
        task_id="create_database",
        python_callable=create_database_and_tables,
        op_kwargs={'cursor': cursor}
    )

    # Task that performs the function that updates the daily data of the "covid_states" table
    update_states_table = PythonOperator(
        task_id="update_states_table",
        python_callable=update_data_covid_states,
        op_kwargs={'cursor': cursor}
    )

    # Task that performs the function that updates the daily data of the "covid_brazil" table
    update_brazil_table = PythonOperator(
        task_id="update_brazil_table",
        python_callable=update_data_covid_brazil,
        op_kwargs={'cursor': cursor}
    )
    
    commit_and_close_connection = PythonOperator(
    	task_id="commit_and_close_connection",
    	python_callable=commit_and_close_connection,
    	op_kwargs={'connection': connection, 'cursor': cursor}
    )

    # Organizes the dependency
    create_database >> [update_states_table, update_brazil_table] >> commit_and_close_connection

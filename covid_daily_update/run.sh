#!/bin/bash
# This script set the environment within the container.

# Update pip
<<<<<<< HEAD
docker exec covid_daily_update_airflow-webserver_1 python3 -m pip install --upgrade pip

# Installs the required libraries in the container environment
docker exec covid_daily_update_airflow-webserver_1 pip install -r /opt/airflow/project/requiriments.txt

# Runs the script that creates the database and its tables, if they do not stretch and populate then with daily data
docker exec covid_daily_update_airflow-webserver_1 python3 /opt/airflow/project/run.py

# Unpause the "daily_update_covid_tables" Dag
docker exec covid_daily_update_airflow-webserver_1 airflow dags unpause daily_update_covid_tables
=======
#docker exec covid_daily_update_airflow-webserver_1 python3 -m pip install --upgrade pip

# Installs the required libraries in the container environment
#docker exec covid_daily_update_airflow-webserver_1 pip install -r /opt/airflow/project/requiriments.txt

# Runs the script that creates the database and its tables, if they do not stretch
docker exec covid_daily_update_airflow-webserver_1 python3 /opt/airflow/project/run.py

>>>>>>> 545278a5cbfa48e0118034f19fe8744429562b55

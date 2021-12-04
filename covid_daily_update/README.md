# Project: Covid Daily Update
OBJECTIVE: Creates two tables in "Covid_Daily_Update" database, in Postgres and populate then with daily data of Covid-19 in Brazil and states. The table "covid_brazil" contains daily covid data in Brazil, and the "covid_states" table contains daily covid data for each Brazilian state.

 First, the two tables are created, then several requests are made in the covid-api API [covid-api](http://covid-api.com/api/), so that daily data about covid is entered in the tables, since the first time there was available data.
 
 # Here is a preview of each of the two tables within the database.

#### "covid_brazil": Contains daily covid data in Brazil.

| date       | confirmed_accumulated                 | confirmated_difference                                 | deaths_accumulated                     | deaths_difference                                       | last_update       |
|------------|---------------------------------------|--------------------------------------------------------|----------------------------------------|---------------------------------------------------------|-------------------|
| Data date. | Cumulative number of confirmed cases. | Difference of confirmed cases from yesterday to today. | Cumulative number of confirmed deaths. | Difference of confirmed deaths from yesterday to today. | Last data update. |

#### "covid_states": Contains daily Covid data from Brazilian states.

| state  | date       | confirmed_accumulated                 | confirmated_difference                                 | deaths_accumulated                     | deaths_difference                                       | last_update       |
|--------|------------|---------------------------------------|--------------------------------------------------------|----------------------------------------|---------------------------------------------------------|-------------------|
| State. | Data date. | Cumulative number of confirmed cases. | Difference of confirmed cases from yesterday to today. | Cumulative number of confirmed deaths. | Difference of confirmed deaths from yesterday to today. | Last data update. |
---
The "run.sh" script set the environment inside the container.

---
The "run.py" script creates the two tables if they do not exist, so it makes several requests in the API to add daily Covid data to the two tables from the first day they were available until the day before the script was run.

---
In addition, within the "dag.py" file there is an Airflow DAG that adds daily Covid data from the previous day to the two database tables.

---
# How to use this project:

##### Prerequisites: Have [Docker](https://www.docker.com) and [Docker Compose](https://docs.docker.com/compose/install/#install-compose) installed on your machine. The docker image is available [here](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml)

---
1. Run the following command in "covid_daily_update" folder:
    ```sh
    echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
    ```

---
2. Run the following command in "covid_daily_update" folder:
- The container will run in background mode, Airflow services on port 8080, and Postgres on port 5434.

    ```sh
    sudo docker-compose up -d
    ```
- Wait a minute for the services to start completely, and then execute the other commands.

---
3. Inside the "covid_daily_update" folder run the file "run.sh":
    ###### WARNING: Run this file only once, even if you stop the container some time.

- It update the "pip", installs the libraries within the file "requiriments.txt".
- Finally unpause the "daily_update_covid_tables" DAG.

    ```sh
    bash run.sh
    ```
---
4. Run the command:
    
- Runs the script that creates the two tables if they do not stretch and populate then with all daily data avaiable in the API.

    ```sh
    sudo docker exec covid_daily_update_airflow-webserver_1 python3 /opt/airflow/project/run.py
    ```

---
5. Now the data will be inserted into the Database tables and Airflow will run in the background, so daily at UTC 13:01 data from the previous day will be added.
- If you prefer, go to the following link "localhost:8080" to access the Airflow UI, the user and password are both "airflow".

---
6. Postgres is running in port 5434, the user and password are both "airflow".
---

## Additional commands:

#### Show the active containers.
```sh
sudo docker ps
```

---
#### Stop the containers (Run in "covid_daily_update" folder).
```sh
sudo docker-compose down
``` 
---
#### Run a command inside the container.
```sh
sudo docker exec covid_daily_update_airflow-webserver_1 <command>
```

---
#### Show logs from a container
```sh
sudo docker logs <container name>
```
---

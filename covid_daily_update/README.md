# Project: Covid Daily Update
OBJECTIVE: Creates a database in SQLite with two tables, "covid_brazil", which contains daily covid data in Brazil, and the "covid_states" table that contains daily covid data for each Brazilian state.

 First, the database file ("database.db") is created, then several requests are made in the covid-api API [covid-api](http://covid-api.com/api/) , so that daily data about covid is entered in the tables, since the first time there was available data.
 
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
The "run.py" script creates the Database and its two tables if they do not exist, so it makes several requests in the API to add daily Covid data to the two tables from the first day they were available until the day before the script was run.

---
In addition, within the "dag.py" file there is an Airflow DAG that adds daily Covid data from the previous day to the two database tables.

---
# How to use this project:

##### Prerequisites: Have [Docker](https://www.docker.com) and [Docker Compose](https://docs.docker.com/compose/install/#install-compose) installed on your machine.

1. Run the following command.
- The container will run in background mode, Airflow services on port 8080, and Postgres on port 5434.
    ```sh
    docker-compose up -d
    ```
---
2. Inside the "covid_daily_update" folder run the file "run.sh":
    ###### WARNING: Run this file only once, even if you stop the container some time.
- It update the "pip", installs the libraries within the file "requiriments.txt".
- Finally it runs the "run.py" file, which creates the Database and its tables if they do not exist. Then it adds within covid's daily database from the first time it became available until the date before the Script was run.
    ```sh
    bash run.sh
    ```
---
3. Now the data will be inserted into the Database tables and Airflow will run in the background, so daily at 13:01 data from the previous day will be added.
- If you prefer, go to the following link "localhost:8080" to access the Airflow UI, the user and password are both "airflow".
---
4. The database is in the "project/data/database/database.db" path.
- You can use some framework that can connect to the Database file to explore it or anything you want.
---

## Additional commands:

#### Show the active containers.
```sh
docker ps
```

---
#### Stop the containers.
```sh
docker-compose down
``` 
---
#### Run a command inside the container.
```sh
docker exec airflow_airflow-webserver_1 <command>
```

---
#### Show logs from a container
```sh
docker logs <container name>
```
---
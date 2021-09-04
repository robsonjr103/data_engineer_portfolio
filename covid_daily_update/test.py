import requests
import sqlite3
import timeit
import os
import pandas as pd
from datetime import datetime

#! Database connection
# conection = sqlite3.connect("data/database/database.db")
# cursor = conection.cursor()

#! API configuration
API_URL = "http://covid-api.com/api/reports/total"

query = {"date": "2020-02-26", "q": "Brazil",
         "region_name": "Brazil", "iso": "BRA"}


def show_covid_states(cursor):
    cursor.execute("SELECT * FROM covid_states")
    print(cursor.fetchall())


def show_covid_brazil(cursor):
    cursor.execute("SELECT * FROM covid_brazil")
    print(cursor.fetchall())

    conection.close()


def print_api_json(API_URL, query):
    json = requests.request("GET", API_URL, params=query).json()["data"]

    # json = response.json()
    # print(json['data'])
    # print(json)
    root_dir = os.getcwd()
    print(root_dir)


def teste():
    date_list = pd.date_range(
        start="2020-05-20", end=datetime.today()).tolist()

    #! Loop that add data in the table "covid_states" in database
    # First Loop: Makes a request in the API for a date within the "date_list" list and returns a JSON with information about all states from that date
    for date in date_list:
        print(str(date)[:10])


if __name__ == "__main__":
    print_api_json(API_URL, query)
    # cursor.execute("DELETE FROM covid_states")
    # teste()
    # show_covid_states(cursor)
    # print()
    # print()
    # show_covid_brazil(cursor)

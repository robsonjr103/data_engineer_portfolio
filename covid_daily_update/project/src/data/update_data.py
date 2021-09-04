# The "update_data_covid_states" function adds data of the yesterday's date to the "covid_states" table. It makes a API request
# with Covid data from each Brazilian state

# The "update_data_covid_brazil" function adds data of the yesterday's date to the "covid_states" table. It makes a API request
# with Covid data from Brazil

def update_data_covid_states(path):
    """
    Summary: Adds in the table "covid_states" daily data of Covid to home Brazilian state.

    * It first connects to the database and creates a cursor to change it.
    * Second sets the API base URL and make a request
    * Third creates a loop that adds the data returned from JSON response to the "covid_states" table of the data collection.

    Args:
      path: Path to the "project" directory.
    """

    import requests
    import sqlite3
    from datetime import datetime, timedelta

    #! Database connection
    # Creates a connection to the database
    conection = sqlite3.connect(f"{path}/data/database/database.db")
    cursor = conection.cursor()  # Creates a cursor to the connection

    #! Define API URL and parameters and make the request
    # Base Api Url
    API_URL = "http://covid-api.com/api/reports"

    # Identifies yesterday's date and formats it to a format that can be used in the API query ("YYYY-mm-dd")
    date = str((datetime.today() - timedelta(days=1)))[0:10]

    # Makes a request in the API for the date and returns a JSON with information about all states from that date
    query = {"date": date, "q": "Brazil",
             "region_name": "Brazil", "iso": "BRA"}

    json = requests.request("GET", API_URL, params=query).json()["data"]

    #! Define which data of which line
    for i in range(0, 27):
        state = json[i]["region"]["province"]
        confirmated = json[i]["confirmed"]
        deaths = json[i]["deaths"]
        last_update = json[i]["last_update"]
        confirmated_difference = json[i]["confirmed_diff"]
        deaths_difference = json[i]["deaths_diff"]

        #! Add the Covid data of the state
        cursor.execute(
            f"INSERT INTO covid_states VALUES ('{state}', '{date}', {confirmated}, {confirmated_difference}, {deaths}, {deaths_difference}, '{last_update}')")

    conection.commit()  # Commit alterations in Database
    conection.close()  # Close connection with Database

    return None


def update_data_covid_brazil(path):
    """
    Summary: It populaes the "covid_brazil" table with daily Covid data from Brazil

    * It first connects to the database and creates a cursor to change it.
    * Second sets the API base URL and make a request
    * Adds the data returned from the JSON response to the "covid_brazil" table of the data collection.

    Args:
      : path (str): Path to the "project" directory.
    """

    import requests
    import sqlite3
    from datetime import datetime, timedelta

    #! Database connection
    # Creates a connection to the database
    conection = sqlite3.connect(f"{path}/data/database/database.db")
    cursor = conection.cursor()  # Creates a cursor to the connection

    #! Define API URL and parameters and make the request
    API_URL = "http://covid-api.com/api/reports/total"

    # Identifies yesterday's date and formats it to a format that can be used in the API query ("YYYY-mm-dd")
    date = str((datetime.today() - timedelta(days=1)))[0:10]

    query = {"date": date, "q": "Brazil",
             "region_name": "Brazil", "iso": "BRA"}

    json = requests.request("GET", API_URL, params=query).json()["data"]

    #! Define which data of which line
    confirmated = json["confirmed"]
    deaths = json["deaths"]
    last_update = json["last_update"]
    confirmated_difference = json["confirmed_diff"]
    deaths_difference = json["deaths_diff"]

    #! Add the Covid data of the date
    cursor.execute(
        f"INSERT INTO covid_brazil VALUES ('{date}', {confirmated}, {confirmated_difference}, {deaths}, {deaths_difference}, '{last_update}')")

    conection.commit()  # Commit alterations in Database
    conection.close()  # Close connection with Database

    return None

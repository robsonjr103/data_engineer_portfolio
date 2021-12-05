import psycopg2

    #! Database connection parameters
_DB_NAME = "olist_database" # Database Name
_DB_USER = "username" # User name
_DB_PASS = "password" # User password   
_DB_HOST = "localhost" # Host of database
PORT = "5434" # Port

    # Create connection and cursor with the database
connection = psycopg2.connect(dbname=_DB_NAME, user=_DB_USER, password=_DB_PASS, host=_DB_HOST, port=PORT)
cursor = connection.cursor()
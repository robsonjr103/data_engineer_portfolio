# This file contains the function "populate_tables" that populate the olist database with data from the CSV files of the folder "data/olist_datasets"


def populate_olist_tables(cursor, files=list):
    """
    Summary: It populaes the Olist Database tables with Olist CSV data.

    * First, a loop is created that defines which table should copy the data from its file.
    * Secondly copy the data.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
      : files (Python List): List of CSV files with data
    """

    # Loop that copy data from CSV files to tables
    for file in files:
      
      # If the file name is not "product_category_name_translation.csv", it will cut the file name and turn the name of the table that will be added the data
      if file != "product_category_name_translation.csv":
          table = file[6:-12]

      # If the file name is "product_category_name_translation.csv", the table name is the file name without the extension ".csv"
      else:
          table = file[:-4]

      # Copy the data from the CSV file to the respective table
      cursor.execute("""
                        
                        COPY {table} FROM '/project/data/olist_datasets/{file}' USING DELIMITERS ',' CSV HEADER;

      """.format(table=table, file=file))



if __name__ == "__main__":

    import psycopg2
    import os

    #! Database connection parameters
    _DB_NAME = "olist_database" # Database Name
    _DB_USER = "username" # User name
    _DB_PASS = "password" # User password   
    _DB_HOST = "localhost" # Host of database
    PORT = "5434" # Port

    # Create connection and cursor with the database
    connection = psycopg2.connect(dbname=_DB_NAME, user=_DB_USER, password=_DB_PASS, host=_DB_HOST, port=PORT)
    cursor = connection.cursor()

    files = os.listdir("/home/diogovalentte/everthing/Projects/GitHub/data_enginner_portfolio/olist_data_warehouse/project/data/olist_datasets")

    populate_olist_tables(cursor=cursor, files=files)

    connection.commit()
    cursor.close()
    connection.close()
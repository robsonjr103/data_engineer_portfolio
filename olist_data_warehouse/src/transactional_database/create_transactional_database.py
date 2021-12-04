# This file contains the function "create_tables" that create the transactional database, it tables, relations, etc.

def create_tables(cursor):
    """
    Summary: Creates the Olist Database tables if them do not exist.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    #! Creates the Olist Database tables if they do not exist.

    # Create table "customers" for the "olist_customers_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                            customer_id CHAR(32) NOT NULL,
                            customer_unique_id CHAR(32) NOT NULL,
                            customer_zip_code_prefix CHAR(5) NOT NULL,
                            customer_city VARCHAR(40) NOT NULL,
                            customer_state VARCHAR(20) NOT NULL)
        """)

    # Create table "geolocation" for the "olist_geolocation_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS geolocation (
                            geolocation_zip_code_prefix CHAR(5) NOT NULL,
                            geolocation_lat VARCHAR(30) NOT NULL,
                            geolocation_lng VARCHAR(30) NOT NULL,
                            geolocation_city VARCHAR(40) NOT NULL,
                            geolocation_state VARCHAR(20) NOT NULL)
        """)

    # Create table "order_items" for the "olist_order_items_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS order_items (
                            order_id CHAR(32) NOT NULL,
                            order_item_id SMALLINT NOT NULL,
                            product_id CHAR(32) NOT NULL,
                            seller_id CHAR(32) NOT NULL,
                            shipping_limit_date TIMESTAMP,
                            price NUMERIC(12, 2) NOT NULL,
                            freight_value NUMERIC(12, 2) 
    )""")

    # Create table "order_payments" for the "olist_order_paymentss_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS order_payments (
                            order_id CHAR(32) NOT NULL,
                            payment_sequential NUMERIC(3) NOT NULL,
                            payment_type VARCHAR(20) NOT NULL,
                            payment_installments NUMERIC(3) NOT NULL,
                            payment_value NUMERIC(12, 2) NOT NULL
    )""")

    # Create table "order_reviews" for the "olist_order_reviews_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS order_reviews (
                            review_id CHAR(32) NOT NULL,
                            order_id CHAR(32) NOT NULL,
                            review_score CHAR(1) NOT NULL,
                            review_comment_title TEXT,
                            review_comment_message TEXT,
                            review_creation_date TIMESTAMP NOT NULL,
                            review_answer_timestamp TIMESTAMP
    )""")

    # Create table "orders" for the "olist_orders_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
                            order_id CHAR(32) NOT NULL,
                            customer_id CHAR(32) NOT NULL,
                            order_status VARCHAR(20) NOT NULL,
                            order_purchase_timestamp TIMESTAMP NOT NULL,
                            order_approved_at TIMESTAMP,
                            order_delivered_carrier_date TIMESTAMP,
                            order_delivered_customer_date TIMESTAMP,
                            order_estimated_delivery_date TIMESTAMP
    )""")

    # Create table "products" for the "olist_products_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                            product_id CHAR(32) NOT NULL,
                            product_category_name VARCHAR(60),
                            product_name_lenght NUMERIC(3),
                            product_description_lenght NUMERIC(5),
                            product_photos_qty NUMERIC(2),
                            product_weight_g NUMERIC(5),
                            product_length_cm NUMERIC(6),
                            product_height_cm NUMERIC(6),
                            product_width_cm NUMERIC(6)
    )""")

    # Create table "sellers" for the "olist_sellers_dataset.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS sellers(
                            seller_id CHAR(32) NOT NULL,
                            seller_zip_code_prefix CHAR(5) NOT NULL,
                            seller_city VARCHAR(40) NOT NULL,
                            seller_state VARCHAR(25) NOT NULL
    )""")

    # Create table "product_category_name_translation" for the "product_category_name_translation.csv" file
    cursor.execute("""CREATE TABLE IF NOT EXISTS product_category_name_translation(
                            product_category_name VARCHAR(60) NOT NULL,
                            product_category_name_english VARCHAR(60)
    )""")    

    return None

"""
if __name__ == "__main__":
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


    create_tables(cursor=cursor)

    connection.commit()
    cursor.close()
    connection.close()"""


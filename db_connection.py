import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DatabaseConnection:

    def __init__(self):
        self.connection = None

    def connect(self):

        try:
            self.connection = mysql.connector.connect(
                host=DB_CONFIG['host'],
                port=DB_CONFIG['port'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                database=DB_CONFIG['database'],
                connection_timeout=10
            )

            if self.connection.is_connected():
                logging.info("MySQL Database connected successfully")
                return self.connection

        except Error as e:
            logging.error(f"MySQL Connection Error: {e}")

    def get_cursor(self):

        if self.connection and self.connection.is_connected():
            return self.connection.cursor(dictionary=True)

    def close_connection(self):

        if self.connection and self.connection.is_connected():
            self.connection.close()
            logging.info("Database connection closed successfully")
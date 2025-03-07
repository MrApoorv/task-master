#pip install mysql-connector-python
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error, connect

load_dotenv()

db_config = { "host" : os.getenv("HOST"),
             "database" : os.getenv("DATABASE"),
             "user" : os.getenv("USER"),
             "password" : os.getenv("PASSWORD"),
            }


def get_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
           print(1)
           return connection
        print(0)
        return None
    except Error as e:
        print(f"Error in connectiong to mysql database. \n ERR: {e}")
        return None
    
# get_db()
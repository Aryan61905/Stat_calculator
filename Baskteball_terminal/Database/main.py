import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection successful")
    except Error in e:
        print(f"The error '{e}' coccured")

    return connection

conncection = create_connection("/Users/roy/Desktop/Baskteball_terminal/sm_app.sqlite")


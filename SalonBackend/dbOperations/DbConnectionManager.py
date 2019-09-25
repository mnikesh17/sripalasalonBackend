import os
import this
from os.path import join, dirname

import pymysql
from dotenv import load_dotenv
from pymysql import Error

# try:
#  dbConnection  =  pymysql.connect(user='root', password='root', host='192.168.1.190', database='test', port=3305)
#  db_Info = dbConnection.get_server_info()
#  print("db version = " + str(db_Info))
# except Error as e:
#     print("dbConnection error " + str(e))
dot_env_path = join(dirname(__file__), 'constants.env')
load_dotenv(dot_env_path)
db_connection = None


class DBConnectionManager:
    @staticmethod
    def open_connection():
        try:
            db_connection = pymysql.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASS"), host=os.getenv("DB_IPADDRESS"), database=os.getenv("DB_NAME"), port=os.getenv("DB_PORT"))
            this.db_connection = db_connection
            db_info = db_connection.get_server_info()
            print("db version = " + str(db_info))
            return db_connection
        except Error as e:
            print("dbConnection error: " + str(e))

    @staticmethod
    def close_connection():
        try:
            if db_connection is not None:
                db_connection.close()
            print("dbConnection closed successful")
        except Error as e:
            print("connection closed exception:  " + e)
        finally:
            print("finally block")

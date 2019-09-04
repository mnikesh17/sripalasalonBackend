import datetime
import json
import logging

import mysql
from MySQLdb._exceptions import Error
from flask import Flask
from flask_restful import Api, Resource
from mysql.connector import connection
from time import strftime

log = logging.getLogger('spam_application')
log.setLevel(logging.DEBUG)

app = Flask(__name__)
api = Api(app)
try:
    dbConnection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='test')
    db_Info = dbConnection.get_server_info()
    print("db version = " + db_Info)
except Error as e:
    print("dbConnection error "+e)


class CloseConnection:
    @staticmethod
    def close_connection():
        try:
            dbConnection.close()
            print("dbConnection closed successful")
        except Error as e:
            print("connection closed exception" + e)
        finally:
            print("finally block")


class CurdOperations(Resource):
    def get(self, num):
        cursor = dbConnection.cursor()
        query = "select id,name,created_on from test.test where id = "+str(num)
        cursor.execute(query)
        result = cursor.fetchall()
        res = result[0]
        created_on = res.__getitem__(2)
        print("query executed " + str())
        date_time = created_on.strftime("%m/%d/%Y %H:%M:%S")
        CloseConnection.close_connection()
        return str(res.__getitem__(0)) +","+ str(res.__getitem__(1)) +","+ date_time

    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()


api.add_resource(CurdOperations, '/<int:num>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1700)

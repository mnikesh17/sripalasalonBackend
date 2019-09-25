import datetime
import logging

import pymysql as pymysql
from flask import Flask
from flask_restful import Api, Resource
from mysql.connector import connection, Error

log = logging.getLogger('spam_application')
log.setLevel(logging.DEBUG)

app = Flask(__name__)
api = Api(app)


class DBConnectionManager:
    @staticmethod
    def close_connection():
        try:
            dbConnection.close()
            print("dbConnection closed successful")
        except Error as e:
            print("connection closed exception" + e)
        finally:
            print("finally block")

    @staticmethod
    def open_connection():
        try:
            dbConnection = pymysql.connect(user='root', password='root', host='192.168.1.190', database='test', port=3305)
            db_Info = dbConnection.get_server_info()
            print("db version = " + str(db_Info))
            return dbConnection
        except Error as e:
            print("dbConnection error " + str(e))


class TestOperation(Resource):
    def get(self):
        return "Working"


class login(Resource):
    def get(self, num):
        dbConnection = DBConnectionManager.open_connection()
        cursor = dbConnection.cursor()
        query = "select id,name,created_on from test.test where id = "+str(num)
        cursor.execute(query)
        result = cursor.fetchall()
        res = result[0]
        created_on = res.__getitem__(2)
        print("query executed " + str())
        date_time = created_on.strftime("%m/%d/%Y %H:%M:%S")
        DBConnectionManager.close_connection()
        return str(res.__getitem__(0)) +","+ str(res.__getitem__(1)) +","+ date_time

    def post(self):
        dbConnection = DBConnectionManager.open_connection()
        cursor = dbConnection.cursor()
        query = "select id,name,created_on from test.test where id = " + str(num)
        cursor.execute(query)
        result = cursor.fetchall()
        res = result[0]
        created_on = res.__getitem__(2)
        print("query executed " + str())
        date_time = created_on.strftime("%m/%d/%Y %H:%M:%S")
        DBConnectionManager.close_connection()
        return str(res.__getitem__(0)) + "," + str(res.__getitem__(1)) + "," + date_time

    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()


# api.add_resource(CurdOperations, '/curd/<int:num>')
api.add_resource(TestOperation, '/test')
# api.add_resource(CurdOperations,/)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1700)

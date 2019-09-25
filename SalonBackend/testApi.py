from flask import request
from flask_restful import Resource

from dbOperations import DbConnectionManager


class Test(Resource):
    def get(self):
        return "workinng"

    def post(self):
        request_data = request.json
        name = request_data['name']
        return ""+str(name)


class DBCheck(Resource):
    def get(self):
        connection = DbConnectionManager.open_connection()
        print(str(connection.get_server_info))

        return connection.get_server_info()

from flask import request
from flask_restful import Resource

from dbOperations.DbConnectionManager import DBConnectionManager
from dbOperations.DbQueries import DbQueries


class Login(Resource):
    def get(self):
        return "this api has post method"

    def post(self):
        dbConnection = DBConnectionManager.open_connection()
        request_data = request.json
        email = request_data['name']
        cursor = dbConnection.cursor()
        query = DbQueries.select_query()
        cursor.execute(query)
        result = cursor.fetchall()
        res = result[0]
        created_on = res.__getitem__(2)
        print("query executed " + str())
        date_time = created_on.strftime("%m/%d/%Y %H:%M:%S")
        DBConnectionManager.close_connection()
        return str(res.__getitem__(0)) + "," + str(res.__getitem__(1)) + "," + date_time

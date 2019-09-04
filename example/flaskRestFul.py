from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class   HelloWorld(Resource):
    def get(self):
        return "hey!"

class Krishna(Resource):
    # def get(self):
    #     return "krishna"

    def get(self, num):
        if num == 1:
            return "num 1 selected"
        if num == 2:
            return "num 2 selected"

class Db(Resource):
    def curd(self):
        return 

api.add_resource(HelloWorld, '/')
api.add_resource(Krishna, '/hello/<int:num>')
api.add_resource(Db,'/curd/<int:no>')


if __name__ == '__main__':
    app.run(port=1700, debug=True, host='0.0.0.0')

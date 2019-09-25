from flask import Flask
from flask_restful import Api

import testApi
from services.login import Login

app = Flask(__name__)
api = Api(app)

api.add_resource(Login, '/login')
api.add_resource(testApi.Test, '/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1700)

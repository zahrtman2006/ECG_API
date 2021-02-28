import requests
import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class TestClass(Resource):
    def get(self):
        return {"Hello World!"}


api.add_resource(TestClass, "/test")










if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0")



from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        return {'item' : name}

    def post(self, name):
        item = {'name':name, 'price':12.00}
        items.append(item)


api.add_resource(Student, '/item/<string:name>')

app.run(port=5000)

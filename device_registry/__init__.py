"""import markdown
import os"""
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("trucks.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


"""
@app.route('/')
def index():
    """"""Present some Documentation""""""
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markD_fil:

        # Read the content of the file
        content = markD_fil.read()

        # Convert to HTML
        return markdown.markdown(content)
"""


class TruckList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        trucks = []

        for key in keys:
            trucks.append(shelf[key])

        return{'message': 'Success', 'data': trucks}, 200

    def post(self):
        parser = reqparse.RequestParser()
        shelf = get_db()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('truck_type', required=True)
        parser.add_argument('controller_gateway', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        if args['identifier'] in shelf:
            print("Truck already exist")
            shelf[args['identifier']] = args
            return {'message': 'Truck already exist', 'data': args}, 404
        else:
            print("New Truck registered")
            shelf[args['identifier']] = args
            return {'message': 'New truck registered', 'data': args}, 201

    def delete(self):
        shelf = get_db()
        keys = list(shelf.keys())

        # trucks = []

        for key in keys:
            print(shelf[key], "deleted")
            del shelf[key]

        # del shelf[identifier]
        return '', 204


class Truck(Resource):
    def get(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Truck not found', 'data': {}}, 404

        return {'message': 'Truck found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Truck not found', 'data': {}}, 404

        del shelf[identifier]
        return {'message': 'Truck deleted'}, 202


api.add_resource(TruckList, '/trucks')
api.add_resource(Truck, '/truck/<string:identifier>')

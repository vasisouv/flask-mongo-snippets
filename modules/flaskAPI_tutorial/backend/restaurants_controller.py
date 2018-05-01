from flask_restful import Resource
from modules.flaskAPI_tutorial.backend import db


class RestaurantsController(Resource):
    def get(self):
        return list(db.find(collection_name='restaurants', limit=10))

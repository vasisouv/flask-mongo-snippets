import json
import os

from bson import json_util
from flask import Response
from flask_restful import Resource, reqparse

script_dir = os.path.dirname(__file__)

parser = reqparse.RequestParser()


class RestaurantsController(Resource):
    def get(self):
        parser.add_argument('area', type=str, required=False, help='Error when parsing area')
        parser.add_argument('min_rating', type=float, required=False, help='Error when parsing min rating')

        args = parser.parse_args()
        area = args['area']
        min_rating = args['min_rating']

        restaurants = self.__get_all_restaurants__()

        # Check if the area was provided, since it was not mandatory (required=False)
        if area:
            restaurants = self.__get_restaurant_by_area__(restaurants=restaurants, area=area)
        # Check if the min_rating was provided
        if min_rating:
            # An error code example: Return error code 400 if the min_rating is below zero
            if min_rating < 0:
                return {'Error': 'min_rating cannot be a negative value'}, 400
            restaurants = self.__get_restaurants_by_min_rating__(restaurants=restaurants, min_rating=min_rating)
        return Response(json.dumps(restaurants, default=json_util.default), mimetype='application/json')

    @staticmethod
    def __get_all_restaurants__():
        with open(script_dir + '/restaurants.json', 'r', encoding='utf-8') as f:
            restaurants = json.load(f)
        f.close()
        return restaurants

    @staticmethod
    def __get_restaurant_by_area__(restaurants, area):

        area = area.lower()
        valid_restaurants = []
        for restaurant in restaurants:
            if restaurant['area'].lower() == area:
                valid_restaurants.append(restaurant)

        return valid_restaurants

    @staticmethod
    def __get_restaurants_by_min_rating__(restaurants, min_rating):
        valid_restaurants = []
        for restaurant in restaurants:
            if restaurant['average_rating'] >= min_rating:
                valid_restaurants.append(restaurant)
        return valid_restaurants

import os

from flask_restful import Resource, reqparse

script_dir = os.path.dirname(__file__)

parser = reqparse.RequestParser()


class ReviewsController(Resource):
    def post(self):
        parser.add_argument('text', type=str, required=True, help='Error when parsing review text')
        parser.add_argument('restaurant_name', type=str, required=True,
                            help='Error when parsing the name of the restaurant')

        args = parser.parse_args()
        review_text = args['text']
        restaurant_name = args['restaurant_name']

        self.__add_new_review__(review_text=review_text, restaurant_name=restaurant_name)

        return {'status': 'Review saved successfully'}, 200

    @staticmethod
    def __add_new_review__(review_text, restaurant_name):
        with open(script_dir + '/reviews.txt', 'a', encoding='utf-8') as f:
            f.write(restaurant_name + " | " + review_text + '\n')
        f.close()

from flask_restful import Resource, request, reqparse
from modules.flaskAPI_tutorial.backend import db

parser = reqparse.RequestParser()


class PMSController(Resource):
    def get(self):
        parser.add_argument('classroom', type=int, required=True, help='Error when parsing classroom')
        args = parser.parse_args()

        response = {
            'classroom': 'Classroom ' + str(args['classroom'])
        }

        return response

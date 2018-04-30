from flask_restful import Resource, request, reqparse
from modules.flaskAPI_tutorial.backend import db

parser = reqparse.RequestParser()


class PMSController(Resource):
    def get(self):
        parser.add_argument('professor_id', type=int, required=True, help='Error when parsing professor name')
        args = parser.parse_args()

        response = {
            'mood': 'https://imgur.com/a/e1wB10E'
        }

        if args['professor_id'] is 1:
            response['professor_name'] = 'Athena Vakali'
        elif args['professor_id'] is 2:
            response['professor_name'] = 'Konstantinos Tsichlas'
        else:
            response['professor_name'] = 'Unknown professor'

        return response

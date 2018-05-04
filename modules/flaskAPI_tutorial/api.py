from flask import Flask
from flask_restful import Api
from modules.flaskAPI_tutorial.backend.restaurants_controller import RestaurantsController
from modules.flaskAPI_tutorial.backend.pms_controller import PMSController

app = Flask(__name__)

# Initialize the API endpoints
api = Api(app)
api.add_resource(RestaurantsController, "/api/restaurants", endpoint="restaurants")
api.add_resource(PMSController, "/api/pms", endpoint="pms")

if __name__ == "__main__":
    # public
    # app.run(debug=True, host='0.0.0.0', port=5110)

    # localhost
    app.run(debug=True, host='127.0.0.1', port=5110)

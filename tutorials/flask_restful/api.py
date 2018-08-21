from flask import Flask
from flask_restful import Api
from tutorials.flask_restful.backend.restaurants_controller import RestaurantsController

app = Flask(__name__)

# Initialize the API endpoints
api = Api(app)
api.add_resource(RestaurantsController, "/api/restaurants", endpoint="restaurants_endpoint")


if __name__ == "__main__":
    # public API
    # app.run(debug=True, host='0.0.0.0', port=5110)

    # localhost API
    app.run(debug=True, host='127.0.0.1', port=5110)

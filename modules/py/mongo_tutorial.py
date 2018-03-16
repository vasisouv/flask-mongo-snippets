import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['yelp']


def insert_to_db(json_obj, collection_name):
    db[collection_name].insert(json_obj)


def find_all_restaurants():
    return db['restaurants'].find({})


def find_restaurants_by_neighborhood(neighborhood):
    return db['restaurants'].find({'neighborhood': neighborhood})


def find_restaurant_by_id(restaurant_id):
    return db['restaurants'].find_one({'business_id': restaurant_id})


def find_restaurant_5_star_reviews(restaurant_id):
    return db['reviews'].find({"$and": [{"business_id": restaurant_id}, {"stars": 5}]})


if __name__ == '__main__':

    # Simple Queries
    # Find all restaurants that belong to a neighbourhood
    restaurants = find_restaurants_by_neighborhood('Downtown')
    print("All restaurants in Downtown")
    for restaurant in restaurants:
        print(restaurant)

    # Find a restaurant by its id
    # id 'v0byOL8VL6v6muGa1anxFA' corresponds to "The Hummus Factory"
    restaurant = find_restaurant_by_id('v0byOL8VL6v6muGa1anxFA')
    # Access the entire json object
    print("The entire object of the Hummus Factory:")
    print(restaurant)
    # Access specific properties of an object
    print(restaurant['neighborhood'])

    # Find all 5-star reviews of a restaurant

    reviews = find_restaurant_5_star_reviews('v0byOL8VL6v6muGa1anxFA')
    print("All fivestar reviews of the Hummus Factory")
    for review in reviews:
        print(review)

    ### Find the coordinates for each restaurant and save them to an external collection
    all_restaurants = find_all_restaurants()
    for restaurant in all_restaurants:
        json_obj = {
            'name': restaurant['name'],
            'business_id': restaurant['business_id'],
            'longitude': restaurant['longitude'],
            'latitude': restaurant['latitude']
        }
        insert_to_db(json_obj, 'restaurants_coordinates')

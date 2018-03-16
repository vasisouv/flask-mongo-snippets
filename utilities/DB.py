import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['yelp']


class DB:

    def insert_to_db(self, json_object, collection_name):
        db[collection_name].insert(json_object)




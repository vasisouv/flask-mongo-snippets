import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['yelp']


def find(collection_name, limit):
    return db[collection_name].find({}, {'_id': False}).limit(limit)

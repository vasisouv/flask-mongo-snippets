import pymongo


class Db:
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client['todo-db']

    def find_all(self, collection_name: str):
        return self.db[collection_name].find({}, {'_id': False})

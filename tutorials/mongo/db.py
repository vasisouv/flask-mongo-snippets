import pymongo


class Db:

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client['todo-db']

    def insert(self, json_obj):
        self.db['todos'].insert(json_obj)

    def find_all_todos(self):
        return self.db['todos'].find({})

    def find_todos_by_importance(self, importance: int):
        return self.db['todos'].find({'importance': importance})

    def find_todos_that_contain_the_word(self, word: str):
        return self.db['todos'].find({'description': {'$regex': '.*' + word + '.*'}})

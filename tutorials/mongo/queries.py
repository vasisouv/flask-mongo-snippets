from tutorials.mongo.db import Db

db = Db()

if __name__ == '__main__':

    # All todos
    all_todos = db.find_all_todos()
    print("All todos")
    for todo in all_todos:
        print(todo)

    # Find all restaurants that belong to a neighbourhood
    print("All todos with importance 5")
    todos = db.find_todos_by_importance(5)
    for todo in todos:
        print(todo)

    # Find all todos that contain a specific word
    word = 'Buy'
    word_specific_todos = db.find_todos_that_contain_the_word(word)
    print("Todos that contain the word " + word)
    for todo in word_specific_todos:
        print(todo)

    # Insert an object in the database
    # print("Inserting a new object...")
    # json_obj = {
    #     'description': 'Some new object we just created',
    #     'notes': 'Lorem ipsum',
    #     'importance': 1
    # }
    # db.insert(json_obj)

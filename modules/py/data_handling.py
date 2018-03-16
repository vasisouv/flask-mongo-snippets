from utilities import DB

if __name__ == '__main__':
    db = DB.DB()

    test_obj = {
        "funny": 0,
        "user_id": "upnUGtuC5V4qxPoE09G_RQ",
        "review_id": "kEQJP6zkv1VcaM4w8IvwtA",
        "text": "Can't go wrong with a hot dog at any hot of the day. Stop wasting time add get it loaded with sauerkraut!!!",
        "business_id": "VE5KGq9ztCztivwbmjNlTQ",
        "stars": 0,
        "date": "2015-10-16",
        "useful": 0,
        "cool": 0
    }
    db.insert_to_db(test_obj, 'test')

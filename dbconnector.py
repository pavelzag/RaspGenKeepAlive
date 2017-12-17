from os import uname
from pymongo import MongoClient
from configuration import get_db_creds

env = get_db_creds('env')
test_uri = get_db_creds('test_uri')
prod_uri = get_db_creds('prod_uri')


if uname()[1] == 'DietPi':
    client = MongoClient(prod_uri)
    db = client.raspgen
else:
    client = MongoClient(test_uri)
    db = client.raspgen_test
print(db)


def set_keep_alive(time_stamp):
    db.generator_keep_alive.update_one({'_id':'keep_alive'}, {"$set": {"time_stamp": time_stamp}}, upsert=True)


def get_keep_alive():
    cursor = db.generator_keep_alive.find({})
    for document in cursor:
        return document

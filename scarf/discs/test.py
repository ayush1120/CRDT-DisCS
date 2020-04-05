import mongoengine
import datetime
import sys
sys.path.append('..')

from discs.settings import NUM_DATABASES

class User(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    userid = mongoengine.ObjectIdField()
    name = mongoengine.StringField(required=true)
    nationility = mongoengine.StringField(required=true)
    age = mongoengine.IntField(required=true, min_value=1)
    friend = mongoengine.StringField()

    # meta = {
    #     'db_alias': 'db1'
    #     'collection': 'user'
    # }

if __name__ == "__main__":

    print(NUM_DATABASES)
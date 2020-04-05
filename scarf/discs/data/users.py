import datetime
import mongoengine

class User(mongoengine.Document):
    user_id = mongoengine.StringField(unique=True)
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    age = mongoengine.IntField(required=True, min_value=1)
    nationality = mongoengine.StringField(required=True)
    
    
    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }

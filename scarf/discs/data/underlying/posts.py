import datetime
import mongoengine 

class Post(mongoengine.Document):
    owner = mongoengine.StringField()
    creation_time = mongoengine.DateTimeField(default=datetime.datetime.now)
    content = mongoengine.StringField(required=True, max_length=20000)
    likes = mongoengine.IntField(min_value=0)

    meta = {
        'db_alias': 'core',
        'collection': 'posts'
    }

import mongoengine

class Followers_update(mongoengine.Document):
    user_name = mongoengine.StringField(unique=True)
    update = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'followers_update'
    }

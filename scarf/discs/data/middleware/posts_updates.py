import mongoengine

class Posts_update(mongoengine.Document):
    username = mongoengine.StringField()
    update = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'posts_update'
    }

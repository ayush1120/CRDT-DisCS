import mongoengine

class Nationality_update(mongoengine.Document):
    user_name = mongoengine.StringField(unique=True)
    update = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'nationality_update'
    }

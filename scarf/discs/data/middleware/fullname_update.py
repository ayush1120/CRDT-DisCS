import mongoengine

class Fullname_update(mongoengine.Document):
    username = mongoengine.StringField(unique=True)
    update_value = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'fullname_update'
    }

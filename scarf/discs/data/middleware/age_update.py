import mongoengine

class Age_update(mongoengine.Document):
    user_name = mongoengine.StringField(unique=True)
    update = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'age_update'
    }

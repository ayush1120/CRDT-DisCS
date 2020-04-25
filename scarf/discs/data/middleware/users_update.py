import mongoengine

class Users_update(mongoengine.Document): 
    users = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'users_update'
    }

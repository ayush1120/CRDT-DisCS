import mongoengine

class Followers_update(mongoengine.Document):

    """
    username : this user is being chosen as follower

    """

    username = mongoengine.StringField(unique=True)
    update_value = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'followers_update'
    }

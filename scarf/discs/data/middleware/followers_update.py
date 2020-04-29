import mongoengine

class Followers_update(mongoengine.Document):

    """
    user_name : this user is being chosen as follower

    """

    user_name = mongoengine.StringField(unique=True)
    update_value = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'followers_update'
    }

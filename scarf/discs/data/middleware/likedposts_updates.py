import mongoengine

class LikedPosts_update(mongoengine.Document):
    id = mongoengine.ObjectIdField()
    post_id = mongoengine.IntField()    # need to be checked
    username = mongoengine.StringField()
    update = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'likedposts_update'
    }

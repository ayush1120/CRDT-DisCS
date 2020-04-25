import mongoengine

class Post_content_update(mongoengine.Document):
    # id = mongoengine.ObjectIdField()
    post_id = mongoengine.IntField()    # need to be checked
    update = mongoengine.StringField()
    
    meta = {
        'db_alias': 'middle',
        'collection': 'post_content_update'
    }

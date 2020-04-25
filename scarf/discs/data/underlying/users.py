import datetime
import mongoengine

class User(mongoengine.Document):
    username = mongoengine.StringField(required=True, unique=True)
    name = mongoengine.StringField(required=True, max_length=200)
    age = mongoengine.IntField(min_value=1)
    nationality = mongoengine.StringField(default='Indian')
    followers = mongoengine.ListField() # List of Follower Usernames
    following = mongoengine.ListField() # List of Following Usernames
    posts = mongoengine.ListField() # List of Post_ids made by a user
    liked_posts = mongoengine.ListField() # List of Post_ids liked by a user

    @property
    def num_followers(self):
        return len(self.followers)
    
    @property
    def num_following(self):
        return len(self.following)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }

import sys
sys.path.append('../')

from bson import json_util, ObjectId

from discs.services.underlying import databaseWrite as underlyingDatabaseWrite
from discs.services.underlying import databaseRead as underlyingDatabaseRead
from discs.services.middleware import databaseWrite as middlewareDatabaseWrite
from discs.services.middleware import databaseRead as middlewareDatabaseRead



from discs.data.middleware.user_update import User_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.followers_update import Followers_update


from discs.data.underlying.users import User 
from discs.data.underlying.posts import Post


from crdt.CRDT.src.gset import GSet
    from crdt.CRDT.src.twopset import  TwoPSet
    from crdt.CRDT.src.lww import LWW


def add_user_update_to_underlying():
    middleware_users = middlewareDatabaseRead.get_user_updates()
    if middleware_users==None:
        return


    middleware_users_Gset = GSet().loadFromDict(json_util.loads(middleware_users.users))
    
    users = [ User.from_json(element) for element in middleware_users_Gset.payload ]
    
    if len(users) > 0:
        for user in users:
            underlyingDatabaseWrite.add_user_by_object(user)



def merge_users(users):
    middleware_users = middlewareDatabaseRead.get_user_updates()
    if middleware_users==None:
        middleware_user_update = User_update()
        middleware_user_update.users = users
        middleware_user_update.save()
        return


    middleware_users_Gset = GSet().loadFromDict(json_util.loads(middleware_users.users))
    users_Gset = GSet().loadFromDict(json_util.loads(users))
    
    middleware_users_Gset.merge(users_Gset)
    
    middleware_users.users = json_util.dumps(middleware_users_Gset.toDict())
    middleware_users.save()




def merge_Age_Update(username, update_value):

    middleware_age_update = Age_update.objects(username=username).first()

    if middleware_age_update:
        middleware_age_update = Age_update()
        middleware_age_update.username = username
        middleware_age_update.update_value = update_value




def add_followers_update_to_underlying(username):
    """
    username : username of the follower
    """
    follower_updates = Followers_update.objects




def merge_followers_update(username, update_value):
    followers_update = Followers_update.objects(username=username).first()

    if(followers_update==None):
        followers_update = Followers_update()
        followers_update.username = username
        followers_update.update_value = update_value
        followers_update.save()

    followers_update_twoPSet =  TwoPSet().loadFromDict(json_util.loads(followers_update.update_value))
    incoming_update_twoPSet = TwoPSet().loadFromDict(json_util.loads(update_value))
    followers_update_twoPSet.merge(incoming_update_twoPSet)
    followers_update.update_value = json_util.dumps(followers_update_twoPSet.toDict())
    followers_update.save()
    





    
    


import sys
sys.path.append('../../../')

import mongoengine
import json
from bson import json_util


from discs.data.middleware.users_update import Users_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.followers_update import Followers_update

from crdt.CRDT.src.gset import GSet
from crdt.CRDT.src.lww import LWW
from crdt.CRDT.src.twopset import TwoPSet



def get_user_update_msg(user):

    user_update = Users_update()
    user_Gset = GSet()
    user_Gset.add(user.to_json())
    user_update.users = json_util.dumps(user_Gset.toDict())

    msg = {
        "type": 'Users_update',
        "data": {'users' : user_update.users}
    }
    return json_util.dumps(msg)

def get_age_update_msg(username, age):
    # data = []
    age_update = Age_update()
    age_lww = LWW()
    age_lww.add(age)
    # for obj in Age_update.objects():
    #     data.append({
    #         'username' : obj.username,
    #         'update_value' : obj.update_value
    #     }) 
    # print(type(age_lww))
    msg = {
        'type' : 'Age_update',
        'data' : {
            'username' : username, 
            'update_value' : json_util.dumps(age_lww.__dict__)
            }
    }
    return json_util.dumps(msg)

def get_fullname_update_msg(username, fullname):
    fullname_update = Fullname_update()
    fullname_lww = LWW()
    fullname_lww.add(fullname)
    msg = {
        'type' : 'Fullname_update',
        'data' : {'username' : username, 'update_value' : json_util.dumps(fullname_lww.__dict__)}
    }
    return json_util.dumps(msg)

def get_nationality_update_msg(username, nationality):
    nationality_update = Nationality_update()
    nationality_lww = LWW()
    nationality_lww.add(nationality)
    msg = {
        'type' : 'nationality_update',
        'data' : {'username' : username, 'update_value' : json_util.dumps(nationality_lww.__dict__)}
    }
    return json.dumps(msg)

def get_post_updates_msg(username, post, update_type='add'):
    """
    update_type : add/remove

    """

    posts_update = Posts_update()
    posts_update.username = username
    posts_update_twoPset = TwoPSet()
    

    if update_type == 'add':
        posts_update_twoPset.add(post.to_json())
    else:
        posts_update_twoPset.remove(post.to_json())

    
    posts_update.update_value = json_util.dumps(posts_update_twoPset.toDict())

    msg = {
        "type": 'posts_update',
        "data": {
            'username' : username,
            'posts' : posts_update.update_value
            }
        }
    return json_util.dumps(msg)

def get_post_content_updates_msg(post_id, content):
    post_content_update = Post_content_update()
    post_content_lww = LWW()
    post_content_lww.add(post_content)
    msg = {
        'type' : 'post_content_update',
        'data' : {'post_id' : post_id, 'update_value' : json_util.dumps(post_content_lww.__dict__)}
    }
    return json_util.dumps(msg)

def get_likedposts_updates_msg(post_id, username, update_type='liked'):
    
    """
    
    update_type: liked/disliked
    """


    liked_posts_update = LikedPosts_update()
    liked_posts_update.username = username
    liked_posts_twoPSet = TwoPSet()
    
    if update_type == 'liked':
        liked_posts_twoPSet.add(post_id)
    else:
        liked_posts_twoPSet.remove(post_id)

    liked_posts_update.update_value = json_util.dumps(liked_posts_twoPSet.toDict())

    msg = {
        'type' : 'Likedposts_update',
        'data' : {
            'username': liked_posts_update.username,
            'update_value': liked_posts_update.update_value
        }
    }
    return json.dumps(msg)


def get_followers_update_msg(username, follower, update_type='follow'):
    """
    username : this user who is being followed
    follower: username of the person who is clicking the follow button to follow the user with username in first argument
    update_type: follow/unfollow
    """

    followers_update = Followers_update()
    followers_update.username = follower
    username_twoPSet = TwoPSet()
    
    if update_type == 'follow':
        username_twoPSet.add(username)
    else:
        username_twoPSet.remove(username)

    followers_update.update_value = json_util.dumps(username_twoPSet.toDict())

    msg = {
        'type' : 'Followers_update',
        'data' : {
            'username': followers_update.username,
            'update_value': followers_update.update_value
        }
    }
    
    return json.dumps(msg)
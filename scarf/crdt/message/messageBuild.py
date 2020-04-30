import sys
sys.path.append('../../../')

import mongoengine
import json

from discs.data.middleware.user_update import Users_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.followers_update import Followers_update


def get_user_update_msg():
    msg = {
        "type": 'Users_update',
        "data": [ 
             {'users' : Users_update.objects().first().users}
        ]
    }
    return json.dumps(msg)

def get_age_update_msg():
    data = []
    for obj in Age_update.objects():
        data.append({
            'user_name' : obj.username,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Age_update',
        'data' : data
    }
    return json.dumps(msg)

    def get_post_updates_msg():
    data = []
    for obj in Post_update.objects():
        data.append({
            'username' : obj.username,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Post_update',
        'data' : data
    }
    return json.dumps(msg)

    def get_post_content_updates_msg():
    data = []
    for obj in Post_content_update.objects():
        data.append({
            'postid' : obj.postid,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Post_content_update',
        'data' : data
    }
    return json.dumps(msg)

    def get_likedposts_updates_msg():
    data = []
    for obj in Likedposts_update.objects():
        data.append({
            'username' : obj.username,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Likedposts_update',
        'data' : data
    }
    return json.dumps(msg)

    def get_fullname_update_msg():
    data = []
    for obj in Fullname_update.objects():
        data.append({
            'user_name' : obj.username,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Fullname_update',
        'data' : data
    }
    return json.dumps(msg)

    def get_nationality_update_msg():
    data = []
    for obj in Nationality_update.objects():
        data.append({
            'user_name' : obj.username,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Nationality_update',
        'data' : data
    }
    return json.dumps(msg)

    def get_followers_update_msg():
    data = []
    for obj in Followers_update.objects():
        data.append({
            'user_name' : obj.username,
            'update' : obj.update_value
        }) 
    msg = {
        'type' : 'Followers_update',
        'data' : data
    }
    return json.dumps(msg)
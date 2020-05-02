import sys
sys.path.append('../../../')

import mongoengine
import json
from bson import json_util


from discs.data.middleware.user_update import User_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.followers_update import Followers_update


from discs.mergeMiddleware import merge_users, add_user_update_to_underlying



def parse_user_update_msg(msg, **kwargs):

    data = msg["data"]
    users = data['users']
    merge_users(users)
    add_user_update_to_underlying()
    return 


def parse_age_update_msg(msg, **kwargs):
    data = msg["data"]
    username = data['username']
    update_value = data['update_value']
    merge_age_updates(update_value)
    add_user_age_update_to_underlying()
    return 

def parse_fullname_update_msg(msg, **kwargs):
    data = msg["data"]
    username = data['username']
    update_value = data['update_value']
    merge_fullname_updates(update_value)
    add_user_fullname_update_to_underlying()
    return 

def parse_nationality_update_msg(msg):
    data = msg["data"]
    username = data['username']
    update_value = data['update_value']
    merge_nationality_updates(update_value)
    add_user_nationality_update_to_underlying()
    return 

def parse_post_updates_msg(msg, **kwargs):
    data = msg["data"]
    Post_update_objects = []

    for element in data:
        new_object = Post_update()
        new_object.username = element['username']
        new_object.update_value = element['update']
        Post_update_objects.append(element)
    
    return Post_update_objects

def parse_post_content_update_msg(msg):
    data = msg["data"]
    post_id = data['post_id']
    update_value = data['update_value']
    merge_post_content_updates(update_value)
    add_post_content_update_to_underlying()
    return 

def parse_likedposts_updates_msg(msg):
    data = msg["data"]
    Likedposts_update_objects = []

    for element in data:
        new_object = Likedposts_updates()
        new_object.username = element['username']
        new_object.update_value = element['update']
        Likedposts_updates_objects.append(element)

    # for obj in Likedposts_update.objects():
    #     data.append({
    #         'username' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Likedposts_update',
    #     'data' : data
    # }
    return Likedposts_updates_objects

def parse_followers_update_msg(msg):
    data = msg["data"]
    
    usename = data['username']
    update_value = data['update_value']



    # for obj in Followers_update.objects():
    #     data.append({
    #         'username' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Followers_update',
    #     'data' : data
    # }
    return Followers_update_objects



def parse_message(message):
    msg = json_util.loads(message)

    msg_type = msg["type"]

    if msg_type == 'User_update':
        parse_user_update_msg(msg)
    elif msg_type == 'Age_update':
        parse_age_update_msg(msg)
    elif msg_type == 'Post_update':
        parse_post_updates_msg(msg)
    elif msg_type == 'Post_content_update':
        parse_post_content_update_msg(msg)
    elif msg_type == 'Likedposts_update':
        parse_likedposts_updates_msg(msg)
    elif msg_type == 'Fullname_update':
        parse_fullname_update_msg(msg)
    elif msg_type == 'Nationality_update':
        parse_nationality_update_msg(msg)
    elif msg_type == 'Followers_update':
        parse_followers_update_msg(msg)
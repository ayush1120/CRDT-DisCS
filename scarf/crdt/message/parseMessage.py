import sys
sys.path.append('../../../')

import mongoengine
import json

from discs.data.middleware.user_update import User_update
from discs.data.middleware.posts_updates import Posts_update
from discs.data.middleware.age_update import Age_update
from discs.data.middleware.post_content_updates import Post_content_update
from discs.data.middleware.likedposts_updates import LikedPosts_update
from discs.data.middleware.fullname_update import Fullname_update
from discs.data.middleware.nationality_update import Nationality_update
from discs.data.middleware.followers_update import Followers_update


def parse_user_update_msg(msg):
    data = msg["data"]
    users = json.load(data[0]['users'])

    # msg = {
    #     "type": 'User_update',
    #     "data": [ 
    #          {'users' : User_update.objects().first().users}
    #     ]
    # }
    return users

def parse_age_update_msg(msg):
    data = msg["data"]

    Age_update_objects = []

    for element in data:
        new_object = Age_update()
        new_object.user_name = element['user_name']
        new_object.update_value = element['update']
        Age_update_objects.append(element)

    # for obj in Age_update.objects():
    #     data.append({
    #         'user_name' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Age_update',
    #     'data' : data
    # }
    return Age_update_objects

def parse_post_updates_msg(msg):
    data = msg["data"]
    Post_update_objects = []

    for element in data:
        new_object = Post_update()
        new_object.username = element['username']
        new_object.update_value = element['update']
        Post_update_objects.append(element)
    
    # for obj in Post_update.objects():
    #     data.append({
    #         'username' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Post_update',
    #     'data' : data
    # }
    return Post_update_objects

def parse_post_content_update_msg(msg):
    data = msg["data"]
    Post_content_update_objects = []

    for element in data:
        new_object = Post_content_update()
        new_object.postid = element['postid']
        new_object.update_value = element['update']
        Post_content_update_objects.append(element)

    # for obj in Post_content_update.objects():
    #     data.append({
    #         'postid' : obj.postid,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Post_content_update',
    #     'data' : data
    # }
    return Post_content_update_objects

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

def parse_fullname_update_msg(msg):
    data = msg["data"]
    Fullname_update_objects = []

    for element in data:
        new_object = Fullname_update()
        new_object.user_name = element['username']
        new_object.update_value = element['update']
        Fullname_update_objects.append(element)

    # for obj in Fullname_update.objects():
    #     data.append({
    #         'user_name' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Fullname_update',
    #     'data' : data
    # }
    return Fullname_update_objects

def parse_nationality_update_msg(msg):
    data = msg["data"]
    Nationality_update_objects = []

    for element in data:
        new_object = Nationality_update()
        new_object.user_name = element['username']
        new_object.update_value = element['update']
        Nationality_update_objects.append(element)

    # for obj in Nationality_update.objects():
    #     data.append({
    #         'user_name' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Nationality_update',
    #     'data' : data
    # }
    return Nationality_update_objects

def parse_followers_update_msg(msg):
    data = msg["data"]
    Followers_update_objects = []

    for element in data:
        new_object = Followers_update()
        new_object.user_name = element['username']
        new_object.update_value = element['update']
        Followers_update_objects.append(element)


    # for obj in Followers_update.objects():
    #     data.append({
    #         'user_name' : obj.username,
    #         'update' : obj.update_value
    #     }) 
    # msg = {
    #     'type' : 'Followers_update',
    #     'data' : data
    # }
    return Followers_update_objects



def parse_message(msg):
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
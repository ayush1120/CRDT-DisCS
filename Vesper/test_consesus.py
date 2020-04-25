import sys
sys.path.append('../scarf')

from discs.services.underlying import databaseRead
from discs.manageDatabases import deleteDatabase

from discs import populate



def get_add_user_msg(user):
    msg = {
    "type": "add_user",
    "args": {
        "pk" : user.id,
        "name": user.name,
        "username": user.username,
        "nationality": user.nationality,
        "age": user.age
    }
    return msg

def get_add_post_msg(post):
    msg = {
        "type" : "add_post",
        "args" : {
            "author" : post.author,
            "content" : post.content,
            "likes" : post.likes
        }
    }
    return msg

def get_deletePost_msg(post):
    msg = {
        "type" : "deletePost",
        "args": {
            "postid" : post.id,
            "author" : post.author,
            "content" : post.content,
            "likes" : post.likes
        }
    }
    return msg

def get_update_user_name_msg(user):
    msg = {
        "type": "update_user_msg",
        "args": {
            "name": user.name,
            "username": user.username
        }
    }
    return msg

def get_update_user_nationality_msg(user):
    msg = {
        "type": "update_user_nationality",
        "args": {
                "username": user.username,
                "nationality": user.nationality
        }
    }
    return msg

def get_update_user_age_msg(user):
    msg = {
        "type": "update_user_age",
        "args": {
                "username": user.username,
                "age": user.age
    }
    return msg

def get_add_follower_msg(user):
    msg = {
        "type": "add_follower",
        "args": {
                "username": user.username,
                "follower": user.follower
    }
    return msg

def get_remove_follower_msg(user):
    msg = {
        "type": "remove_follower",
        "args": {
                "username": user.username,
                "follower": user.follower
    }
    return msg

def get_change_post_content(post):
    msg = {
        "type": "change_post_content",
        "args": {
                "postid": post.id,
                "content": post.content
    }
    return msg

def get_add_post_likes_msg(post, user):
    msg = {
        "type": "add_post_likes",
        "args": {
                "postid": post.id,
                "username": user.username
    }
    return msg

def get_reduce_post_likes_msg(post, user):
    msg = {
        "type": "reduce_post_likes",
        "args": {
                "postid": post.id,
                "username": user.username
    }
    return msg

if __name__ == "__main__":
    messages = []
    for _ in range(24):
        user = populate.get_fake_user()
        msg = get_add_user_msg(user)
        messages.append(msg)
        
    

    


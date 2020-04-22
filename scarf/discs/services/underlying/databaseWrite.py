import mongoengine
import datetime
import pymongo
from discs.data.underlying.users import User
from discs.data.underlying.posts import Post
from discs.settings import connect_with_database

@connect_with_database
def check_user(name):
    pass


@connect_with_database
def check_post(post_id):
    pass


@connect_with_database
def add_user(name='Sukhiya', username='soku', nationality='Indian', age=20, **kwargs):
    user = User()
    user.full_name = name
    user.username = username
    user.nationality = nationality
    user.age = age
    user.save()
    user_id = user.id
    return user_id

@connect_with_database
def update_user_age(username, age=0, **kwargs):
    if(check_user(username)):
        user = User.objects(username=username).first()
        if(age!=0):     
            user.age=age       
        user.save()

@connect_with_database
def update_user_nationality(username, nationality, **kwargs):
    if(check_user(username)):
        user = User.objects(username=username).first()
        user.nationality = nationality
        user.save()

@connect_with_database
def update_user_fullname(username, fullname, **kwargs):
    if(check_user(username)):
        user = User.objects(username=username).first()
        user.fullname = fullname
        user.save()

@connect_with_database
def add_follower(username, follower, **kwargs):
    """
    username: username of person being followed
    follower: username of follower
    """
    if(check_user(username) and check_user(follower)):
        user = User.objects(username=username).first()
        user.followers.add(follower)
        user.save()
        user1 = User.objects(username=follower).first()
        user1.following.add(username)
        user1.save()

@connect_with_database
def remove_follower(username, follower, **kwargs):
    if(check_user(username)):
        user = User.objects(username=username).first()
        if(follower in user.followers):
            user.followers.remove(follower)
        user.save()
    if(check_user(follower)):
        user1 = User.objects(username=follower).first()
        if(username in user1.following):
            user1.following.remove(username)
        user1.save()

@connect_with_database
def add_post(owner='aush', creation_time=datetime.time, content='This is just the beginning', likes=0, **kwargs):
    """
    Args: 
        owner: username of owner \n 
    Returns : post_id
    """
    if(check_user(owner)):
        post = Post()
        post.owner = owner
        post.creation_time = creation_time
        post.content = content
        post.likes = likes
        post.save()
        post_id = post.id
        user = User.objects(username=owner).first()
        user.posts.add(post_id)
        return post_id
    return "Failed"

@connect_with_database
def change_post_content(post_id, content, **kwargs):
    if(check_post(post_id)):
        post = Post.objects(id=post_id).first()
        post.content = content
        post.save()

@connect_with_database
def add_post_likes(post_id, username, **kwargs):
    if(check_user(username) and check_post(post_id)):
        post = Post.objects(id=post_id).first()
        user = User.objects(username=username).first()
        if(post_id not in user.likedposts):
            post.likes=post.likes+1
            user.likedposts.add(post_id)
        post.save()
        user.save()

@connect_with_database
def reduce_post_likes(post_id, username, **kwargs):
    if(check_user(username) and check_post(post_id)):
        post = Post.objects(id=post_id).first()
        user = User.objects(username=username).first()
        if(post_id in user.likedposts):
            post.likes=post.likes-1
            user.likedposts.remove(post_id)
        post.save()
        user.save()

@connect_with_database
def deletePost(post_id, **kwargs):
    if(check_post(post_id)):
        post = Post.objects(post_id=post_id).first()
        post.delete()

# @connect_with_database
# def changeUserDetails(user_id, name, age, nationality, **kwargs):
#     user = User.objects(user_id=user_id).first()
#     user.name = name
#     user.age = age
#     user.nationality = nationality
#     user.save()
#     return user

# @connect_with_database
# def deleteUser(user_id, **kwargs):
#     user = User.objects(user_id=user_id).first()
#     user.delete()

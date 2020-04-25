import sys
sys.path.append('../../../')

import mongoengine
import datetime
import pymongo
from discs.data.underlying.users import User
from discs.data.underlying.posts import Post
from discs.settings import connect_with_database

@connect_with_database
def check_user(name):
    user = User.objects(username=name).first()
    if user is None:
        return False
    return True

@connect_with_database
def check_post(post_id):
    post = Post.objects(id=post_id).first()
    if post is None:
        return False
    return True


@connect_with_database
def add_user(name='Sukhiya', username='soku', nationality='Indian', age=20, **kwargs):
    """
    Args:
    name: Full Name of the user,
    username: username (should not be already present),
    nationality: nationality,
    age: age

    Returns:
    user_id
    """
    user = User()
    user.name = name
    user.username = username
    user.nationality = nationality
    user.age = age
    user.save()
    user_id = user.id
    return user_id

@connect_with_database
def update_user_age(username, age=0, **kwargs):
    """
    Args:
    username: username,
    age: age

    Returns:
    Boolean - True/False
    """
    if(check_user(username)):
        user = User.objects(username=username).first()
        if(age!=0):     
            user.age=age       
        user.save()
        return True
    return False

@connect_with_database
def update_user_nationality(username, nationality, **kwargs):
    """
    Args:
    username: username,
    nationality: nationality,
    
    Returns:
    Boolean - True/False
    """
    if(check_user(username)):
        user = User.objects(username=username).first()
        user.nationality = nationality
        user.save()
        return True
    return False
    
@connect_with_database
def update_user_name(username, name, **kwargs):
    """
    Args:
    username: username,
    name: Full Name of the user,
    
    Returns:
    Boolean - True/False
    """
    if(check_user(username)):
        user = User.objects(username=username).first()
        user.name = name
        user.save()
        return True
    return False

@connect_with_database
def add_follower(username, follower, **kwargs):
    """
    Args:
    username: username of person being followed,
    follower: username of follower

    Returns:
    Boolean - True/False
    """
    if(check_user(username) and check_user(follower)):
        user = User.objects(username=username).first()
        if follower in user.followers:
            return False
        user.followers.append(follower)
        user.save()
        user1 = User.objects(username=follower).first()
        user1.following.append(username)
        user1.save()
        return True
    return False

@connect_with_database
def remove_follower(username, follower, **kwargs):
    """
    Args:
    username: username of the user being followed,
    follower: username of the follower

    Returns:
    Boolean - True/False
    """
    if(check_user(username)==False or check_user(follower)==False):
        return False
    user = User.objects(username=username).first()
    if(follower in user.followers):
        user.followers.remove(follower)
    user.save()
    user1 = User.objects(username=follower).first()
    if(username in user1.following):
        user1.following.remove(username)
    user1.save()
    return True

@connect_with_database
def add_post(author='aush', creation_time=datetime.datetime.now, content='This is just the beginning', likes=0, **kwargs):
    """
    Args:
    author: username of author of the post,
    creation_time: date and time of creation of the post

    Returns:
    post_id / Error message
    """
    if(check_user(author)):
        post = Post()
        post.author = author
        post.creation_time = creation_time
        post.content = content
        post.likes = likes
        post.save()
        post_id = post.id
        user = User.objects(username=author).first()
        user.posts.append(post_id)
        user.save()
        return post_id
    return "User does not exist"

@connect_with_database
def change_post_content(post_id, content, **kwargs):
    """
    Args:
    post_id: id of the post,
    content: content of the post

    Returns:
    Boolean - True/False
    """
    if(check_post(post_id)):
        post = Post.objects(id=post_id).first()
        post.content = content
        post.save()
        return True
    return False

@connect_with_database
def add_post_likes(post_id, username, **kwargs):
    """
    Args:
    post_id: id of the post,
    username: username of the user liking the post

    Returns:
    Boolean - True/False
    """
    if(check_user(username) and check_post(post_id)):
        post = Post.objects(id=post_id).first()
        user = User.objects(username=username).first()
        if(post_id not in user.liked_posts):
            post.likes=post.likes+1
            user.liked_posts.append(post_id)
        post.save()
        user.save()
        return True
    return False

@connect_with_database
def reduce_post_likes(post_id, username, **kwargs):
    """
    Args:
    post_id: id of the post,
    username: username of the user unliking the post

    Returns:
    Boolean - True/False
    """
    if(check_user(username) and check_post(post_id)):
        post = Post.objects(id=post_id).first()
        user = User.objects(username=username).first()
        if(post_id in user.liked_posts):
            post.likes=post.likes-1
            user.liked_posts.remove(post_id)
        post.save()
        user.save()
        return True
    return False

@connect_with_database
def deletePost(post_id, **kwargs):
    """
    Args:
    post_id: id of the post,
    
    Returns:
    Boolean - True/False
    """
    if(check_post(post_id)):
        post = Post.objects(id=post_id).first()
        post.delete()
        return True
    return False

if __name__ == "__main__":
    from discs.populate import get_fake_user, get_fake_post
    from discs.services.underlying.databaseRead import readUsers, print_users, print_user
    from discs.services.underlying.databaseRead import readPosts, print_posts, print_post
    from discs.data.underlying.users import User 
    from discs.data.underlying.posts import Post
    from discs.manageDatabases import deleteDatabase
    import random

    NUM_FAKE_USERS = 1
    NUM_FAKE_POSTS = 1

    dbName = 'CRDT-DisCS_test'
    for _ in range(NUM_FAKE_USERS):
        user = get_fake_user()
        add_user(name=user.name,
            username=user.username,
            nationality=user.nationality,
            age=user.age,
            dbName=dbName)

    users = readUsers(dbName=dbName)
    print_users(users)

    post_ids = []
    for _ in range(NUM_FAKE_POSTS):
        post = get_fake_post()
        author_index = random.randint(0,len(users)-1)
        post.author = users[0].username
        post_id = add_post(
            author=post.author,
            creation_time=post.creation_time,
            content=post.content,
            dbName=dbName
        )
        post_ids.append(post_id)

    
    myPostID = post_ids[0]

    posts = readPosts(dbName=dbName)
    print_posts(posts)

    print(f'--------Deleting post {myPostID}---------')

    deletePost(post_id=myPostID, dbName=dbName)

    posts = readPosts(dbName=dbName)
    print_posts(posts)


    # print_users(users)
    
    deleteDatabase(dbName=dbName)
 
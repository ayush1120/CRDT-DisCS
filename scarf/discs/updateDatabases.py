import sys
sys.path.append('../')

from discs.services.underlying import databaseWrite as underlyingDatabaseWrite
from discs.services.underlying import databaseRead as underlyingDatabaseRead
from discs.services.middleware import databaseWrite as middlewareDatabaseWrite
from discs.services.middleware import databaseRead as middlewareDatabaseRead

CRDT_UPDATE = True
RAFT_UPDATE = False



# def check_user(name):
#     pass



# def check_post(post_id):
#     pass

def underlyingDatabaseName(index):
    if index==None:
        return None
    return 'CRDT-DisCS_Core_' + str(index) 


def middlewareDatabaseName(index):
    if index==None:
        return None
    return 'CRDT-DisCS_Middle_' + str(index) 



def add_user(name='Sukhiya', username='soku', nationality='Indian', age=20, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    user_id = underlyingDatabaseWrite.add_user(name, username, nationality, age, dbName=dbName)
    
    if user_id is not None:
        user = underlyingDatabaseRead.get_user_by_id(user_id, dbName=dbName)

        if CRDT_UPDATE:
            middlewareDatabaseWrite.update_user(user, dbName=middlewareDBName)



def update_user_age(username, age, dbIndex=None, **kwargs): 
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.update_user_age(username, age, dbName=dbName)
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_age(username, age, dbName=middlewareDBName)
    

def update_user_nationality(username, nationality, dbIndex=None, **kwargs):  
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.update_user_nationality(username, nationality, dbName=dbName)

    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_nationality(username, nationality, dbName=middlewareDBName)



def update_user_name(username, name, dbIndex=None, **kwargs):     
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.update_user_name(username, name, dbName=dbName)
    
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_fullname(username, name, dbName=middlewareDBName)



def add_follower(username, follower, dbIndex=None, **kwargs):
    """
    username : this user who is being followed
    follower: username of the person who is clicking the follow button to follow the user with username in first argument
    """

    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)
    updated = underlyingDatabaseWrite.add_follower(username, follower, dbName=dbName)
    
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_followers(username, follower, dbName=middlewareDBName)


def remove_follower(username, follower, dbIndex=None, **kwargs):
    """
    username : this user who is being followed
    follower: username of the person who is clicking the follow button to follow the user with username in first argument
    """
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)
    updated = underlyingDatabaseWrite.remove_follower(username, follower, dbName=dbIndex)

    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.remove_user_follower(username, follower, dbName=middlewareDBName)


def add_post(author, creation_time, content, likes=0, dbIndex=None, **kwargs):   
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    post_id = underlyingDatabaseWrite.add_post(author, creation_time, content, likes, dbName=dbName)
    
    if CRDT_UPDATE and post_id is not None:
        post = underlyingDatabaseRead.get_post_by_id(post_id, dbName=dbName)
        middlewareDatabaseWrite.add_post(username=author, post=post, dbName=middlewareDBName)

def change_post_content(post_id, content, dbIndex=None, **kwargs): 
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.change_post_content(post_id, content, dbName=dbName)
    if CRDT_UPDATE and updated:
        post = underlyingDatabaseRead.get_post_by_id(post_id, dbName=dbName)
        username = post.author
        middlewareDatabaseWrite.update_post_content(username, post.post_content, dbName=middlewareDBName)

def add_post_likes(post_id, username, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.add_post_likes(post_id, username, dbName=dbName)
    if CRDT_UPDATE and updated:
        liked_post = underlyingDatabaseRead.get_liked_posts_by_username(username, dbName=dbName)
        middlewareDatabaseWrite.add_liked_post(username, liked_post, dbName=middlewareDBName)

def reduce_post_likes(post_id, username, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.reduce_post_likes(post_id, username, dbName=dbName)
    if CRDT_UPDATE and updated:
        liked_post = underlyingDatabaseRead.get_liked_posts_by_username(username, dbName=dbName)
        middlewareDatabaseWrite.remove_liked_post(username, liked_post, dbName=middlewareDBName)

def deletePost(post_id, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.deletePost(post_id, dbName=dbName)
    if CRDT_UPDATE and updated:
        post = underlyingDatabaseRead.get_post_by_id(post_id, dbName=dbName)
        username = post.author
        middlewareDatabaseWrite.remove_post(username, post, dbName=middlewareDBName)



if __name__ == "__main__":
    from discs.populate import get_fake_user, get_fake_post
    from discs.services.underlying.databaseRead import readUsers, print_users, print_user
    from discs.services.underlying.databaseRead import readPosts, print_posts, print_post
    from discs.data.underlying.users import User 
    from discs.data.underlying.posts import Post
    from discs.manageDatabases import deleteDatabase
    from discs.data.middleware.users_update import Users_update 
    from discs.data.middleware.fullname_update import Fullname_update

    from crdt.CRDT.src.gset import GSet
    from crdt.CRDT.src.twopset import  TwoPSet
    from crdt.CRDT.src.lww import LWW

    import random
    import mongoengine
    import json

    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')

    mongoengine.register_connection(alias='core', name='CRDT-DisCS_Test_UDB')
    mongoengine.register_connection(alias='middle', name='CRDT-DisCS_Test_Middle_UDB')
    

    NUM_FAKE_USERS = 1
    NUM_FAKE_POSTS = 2

    dbName = None
    dbName_middleware = None

    for _ in range(NUM_FAKE_USERS):
        user = get_fake_user()
        add_user(name=user.name,
            username=user.username,
            nationality=user.nationality,
            age=user.age)

    users = readUsers(dbName=dbName)
    # print_users(users)
    
    users_update = middlewareDatabaseRead.get_user_updates(dbName=dbName_middleware)
    users_Gset = GSet()
    users_Gset.__dict__ = json.loads(users_update.users)
    users_from_Gset = json.loads(users_update.users)['payload']

    users_loaded = []
    last_user_name = ""
    for element in users_from_Gset:
        user = User.from_json(element, created=True)
        users_loaded.append(user)
        last_user_name = user.username
    
    update_user_name(last_user_name, "Rakesh")

    user_fullname_updates = middlewareDatabaseRead.get_fullname_updates_by_username(last_user_name)
    print(last_user_name, user_fullname_updates.update_value)

    users = readUsers(dbName=dbName)
    print_users(users)

    update_user_age(last_user_name, 101)
    
    user_age_updates = middlewareDatabaseRead.get_age_updates_by_username(username)
    print(last_user_name, user_age_updates)

    users = readUsers(dbName=dbName)
    print_users(users)

    for _ in range(NUM_FAKE_POSTS):
        post = get_fake_post()
        add_post(author=last_user_name, 
            creation_time=post.creation_time, 
            content=post.content, 
            likes=post.likes)

    posts = readPosts(dbName=dbName)
    # print_posts(posts) 

    # print("\nTransition\n")


    posts_updates = middlewareDatabaseRead.get_posts_updates(dbName=dbName_middleware)

    all_posts_added = [] 
    all_posts_removed = []

    print('Num Objects in post_update : ', len(posts_updates))

    for post_update_object in posts_updates:

        update_string = post_update_object.update_value

        updates_TwoPSet = TwoPSet().loadFromDict(json.loads(update_string))

        added_posts_jsons = updates_TwoPSet.addedValues()
        for added_post_json in added_posts_jsons:
            added_post = Post.from_json(added_post_json) 
            all_posts_added.append(added_post)

        removed_posts_jsons = updates_TwoPSet.removedValues()
        for removed_post_json in removed_posts_jsons:
            removed_post = Post.from_json(removed_post_json)
            all_posts_removed.append(removed_post)


    # print('-----------------------------Added Posts-------------------------------')
    # print("Num of all_posts_added : ", len(all_posts_added))
    # print_posts(all_posts_added)
    
    # print('-----------------------------Removed Posts-------------------------------')
    # print_posts(all_posts_removed)
    # all_posts_added = [] 
    # all_posts_removed = []


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
        #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    #     add_post(author=last_user_name, 
    #         creation_time=post.creation_time, 
    #         content=post.content, 
    #         likes=post.likes)
    # posts = readPosts(dbName=dbName)
    # print_posts(posts)
    # print("Hi")


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')
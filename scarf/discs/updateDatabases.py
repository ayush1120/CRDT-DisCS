import sys
sys.path.append('../')

from bson import json_util, ObjectId

from discs.services.underlying import databaseWrite as underlyingDatabaseWrite
from discs.services.underlying import databaseRead as underlyingDatabaseRead
from discs.services.middleware import databaseWrite as middlewareDatabaseWrite
from discs.services.middleware import databaseRead as middlewareDatabaseRead


from crdt.server.client import try_internal_comm

from crdt.message import messageBuild


db_index = 1
server_address =  f'http://0.0.0.0:{str(6000+db_index)}' + '/testSending'

CRDT_UPDATE = True
RAFT_UPDATE = False

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
            msg = messageBuild.get_user_update_msg(user)

            if 'serverNodeIndex' in kwargs:
                serverNodeIndex = kwargs.get('serverNodeIndex')
                if serverNodeIndex is not None:
                    server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                    try_internal_comm(server_address, msg)
            # print('Message : ', msg)



def update_user_age(username, age, dbIndex=None, **kwargs): 
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.update_user_age(username, age, dbName=dbName)
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_age(username, age, dbName=middlewareDBName)
        msg = messageBuild.get_age_update_msg(username, age)

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)
        # print('Message : ', msg)

def update_user_nationality(username, nationality, dbIndex=None, **kwargs):  
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.update_user_nationality(username, nationality, dbName=dbName)

    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_nationality(username, nationality, dbName=middlewareDBName)
        msg = messageBuild.get_nationality_update_msg(username, nationality)

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'


                try_internal_comm(server_address, msg)
        # print('Message : ', msg)


def update_user_name(username, name, dbIndex=None, **kwargs):     
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.update_user_name(username, name, dbName=dbName)
    
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.update_user_fullname(username, name, dbName=middlewareDBName)
        msg = messageBuild.get_fullname_update_msg(username, name)

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)
        # print('Message : ', msg)

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
        msg = messageBuild.get_followers_update_msg(username, follower, update_type='follow')


        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)

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
        msg = messageBuild.get_followers_update_msg(username, follower, update_type='follow')

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)


def add_post(author, creation_time, content, likes=0, dbIndex=None, **kwargs):   
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    post_id = underlyingDatabaseWrite.add_post(author, creation_time, content, likes, dbName=dbName)
    
    if CRDT_UPDATE and post_id is not None:
        post = underlyingDatabaseRead.get_post_by_id(post_id, dbName=dbName)
        middlewareDatabaseWrite.add_post(username=author, post=post, dbName=middlewareDBName)
        msg = messageBuild.get_post_updates_msg(author, post, update_type='add')

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)
        # print('Message : ', msg)

    return post_id

def change_post_content(post_id, content, dbIndex=None, **kwargs): 
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.change_post_content(post_id, content, dbName=dbName)
    if CRDT_UPDATE and updated:
        post = underlyingDatabaseRead.get_post_by_id(post_id, dbName=dbName)
        username = post.author
        middlewareDatabaseWrite.update_post_content(username, post.content, dbName=middlewareDBName)
        msg = messageBuild.get_post_content_updates_msg(post_id, content)

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'    
            
                try_internal_comm(server_address, msg)
        # print('Message : ', msg)

def add_post_likes(post_id, username, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.add_post_likes(post_id, username, dbName=dbName)
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.add_liked_post(username, post_id, dbName=middlewareDBName)
        msg = messageBuild.get_likedposts_updates_msg(post_id, username, update_type='liked')

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)

def reduce_post_likes(post_id, username, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)
    updated = underlyingDatabaseWrite.reduce_post_likes(post_id, username, dbName=dbName)
    if CRDT_UPDATE and updated:
        middlewareDatabaseWrite.remove_liked_post(username, post_id, dbName=middlewareDBName)
        msg = messageBuild.get_likedposts_updates_msg(post_id, username, update_type='disliked')

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)

def deletePost(post_id, dbIndex=None, **kwargs):
    dbName = underlyingDatabaseName(dbIndex)
    middlewareDBName = middlewareDatabaseName(dbIndex)

    updated = underlyingDatabaseWrite.deletePost(post_id, dbName=dbName)
    if CRDT_UPDATE and updated:
        post = underlyingDatabaseRead.get_post_by_id(post_id, dbName=dbName)
        username = post.author
        middlewareDatabaseWrite.remove_post(username, post, dbName=middlewareDBName)
        msg = messageBuild.get_post_updates_msg(author, post, update_type='remove')

        if 'serverNodeIndex' in kwargs:
            serverNodeIndex = kwargs.get('serverNodeIndex')
            if serverNodeIndex is not None:
                server_address =  f'http://0.0.0.0:{str(6000+serverNodeIndex)}' + '/testSending'

                try_internal_comm(server_address, msg)




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
    

    NUM_FAKE_USERS = 2
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
    users_Gset.__dict__ = json_util.loads(users_update.users)
    users_from_Gset = json_util.loads(users_update.users)['payload']

    users_loaded = []
    last_username = ""
    for element in users_from_Gset:
        user = User.from_json(element, created=True)
        users_loaded.append(user)
        last_username = user.username
    
    update_user_name(last_username, "Rakesh")

    user_fullname_updates = middlewareDatabaseRead.get_fullname_updates_by_username(last_username)
    # print(last_username, user_fullname_updates.update_value)

    update_user_age(last_username, 101)
    
    user_age_updates = middlewareDatabaseRead.get_age_updates_by_username(last_username)
    # print(last_username, user_age_updates.update_value)

    update_user_nationality(last_username, "Hungarian")

    user_nationality_updates = middlewareDatabaseRead.get_nationality_updates_by_username(last_username)
    # if(user_nationality_updates is not None):
        # print(last_username, user_nationality_updates.update_value)

    user1 = users[0].username
    user2 = users[1].username
    add_follower(user1, user2)

    users = readUsers(dbName=dbName)
    print_users(users)

    

    last_post_id = None

    for _ in range(NUM_FAKE_POSTS):
        post = get_fake_post()
        last_post_id = add_post(author=last_username, 
            creation_time=post.creation_time, 
            content=post.content, 
            likes=post.likes)

    posts = readPosts(dbName=dbName)
    # print_posts(posts) 

    posts_updates = middlewareDatabaseRead.get_posts_updates(dbName=dbName_middleware)

    all_posts_added = [] 
    all_posts_removed = []

    # print('Num Objects in post_update : ', len(posts_updates))

    for post_update_object in posts_updates:

        update_string = post_update_object.update_value

        updates_TwoPSet = TwoPSet().loadFromDict(json_util.loads(update_string))

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


    change_post_content(last_post_id, "The Red Roses")

    

    # posts = readPosts(dbName=dbName)
    # print_posts(posts) 


    add_post_likes(posts[0].id, last_username)
    add_post_likes(posts[1].id, last_username)
    reduce_post_likes(posts[0].id, last_username)

    liked_post_updates = middlewareDatabaseRead.get_liked_posts_updates_by_username(last_username)
    liked_post_TwoPSet = TwoPSet().loadFromDict(json_util.loads(liked_post_updates.update_value))

    liked_post_TwoPSet.display()

    added_liked_posts = liked_post_TwoPSet.addedValues()
    remove_liked_posts = liked_post_TwoPSet.removedValues()


    # print('added_liked_posts : ', added_liked_posts)
    # print('remove_liked_posts : ', remove_liked_posts)


    posts = readPosts()
    # print_posts(posts)


    post_id1 = added_liked_posts[0]
    # print(post_id1)

    
    followers_update = middlewareDatabaseRead.get_follower_updates_by_username(user1)
    # print(followers_update.update_value)
    followers = TwoPSet().loadFromDict(json_util.loads(followers_update.update_value))

    # followers.display()
    followers_added = followers.addedValues()
    followers_removed = followers.removedValues()

    # print('followers_added: ', followers_added)
    # print('followers_removed: ', followers_removed)



    remove_follower(user1, user2)
    followers_update = middlewareDatabaseRead.get_follower_updates_by_username(user1)
    followers = TwoPSet().loadFromDict(json_util.loads(followers_update.update_value))

    # followers.display()
    followers_added = followers.addedValues()
    followers_removed = followers.removedValues()

    # print('followers_added: ', followers_added)
    # print('followers_removed: ', followers_removed)





    # print('Num of posts : ', len(readPosts()))

    # print_user(underlyingDatabaseRead.get_user_by_username(last_username))

    # print('Object Id : ', ObjectId(post_id[0]['id']))

    # post_object = underlyingDatabaseRead.get_post_by_id(post_id)
    # underlyingDatabaseRead.print_post(post_object) 

    # reduce_post_likes(last_post_id)
    
    # print('-----------------------------Removed Posts-------------------------------')
    # print_posts(all_posts_removed)
    # all_posts_added = [] 
    # all_posts_removed = []

    # change_post_content(last_post_id, "The Red Roses")

    # print('-----------------------------Added Posts-------------------------------')
    # print("Num of all_posts_added : ", len(all_posts_added))
    # print_posts(all_posts_added)


    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')    
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

    updated = underlyingDatabaseWrite.add_post(author, creation_time, content, likes, dbName=dbName)
    
    if CRDT_UPDATE and updated is not None:
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
    import random
    import mongoengine
    import json

    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')

    mongoengine.register_connection(alias='core', name='CRDT-DisCS_Test_UDB')
    mongoengine.register_connection(alias='middle', name='CRDT-DisCS_Test_Middle_UDB')
    

    NUM_FAKE_USERS = 1
    NUM_FAKE_POSTS = 1

    dbName = None
    dbName_middleware = None

    for _ in range(NUM_FAKE_USERS):
        user = get_fake_user()
        add_user(name=user.name,
            username=user.username,
            nationality=user.nationality,
            age=user.age)

    users = readUsers(dbName=dbName)
    print_users(users)
    users_update = middlewareDatabaseRead.get_user_updates(dbName=dbName_middleware)
    print(type(users_update))
    print(users_update.users)
    new_user = User()
    user_read = json.loads(users_update.users)["payload"][0]
    new_user.__dict__ = user_read
    print_user(new_user)

    # post_ids = []
    # for _ in range(NUM_FAKE_POSTS):
    #     post = get_fake_post()
    #     author_index = random.randint(0,len(users)-1)
    #     post.author = users[0].username
    #     post_id = add_post(
    #         author=post.author,
    #         creation_time=post.creation_time,
    #         content=post.content,
    #         dbName=dbName
    #     )
    #     post_ids.append(post_id)

    
    # myPostID = post_ids[0]

    # posts = readPosts(dbName=dbName)
    # print_posts(posts)

    # print(f'--------Deleting post {myPostID}---------')

    # deletePost(post_id=myPostID, dbName=dbName)

    # posts = readPosts(dbName=dbName)
    # print_posts(posts)


    # # print_users(users)
    
    deleteDatabase(dbName='CRDT-DisCS_Test_UDB')
    deleteDatabase(dbName='CRDT-DisCS_Test_Middle_UDB')
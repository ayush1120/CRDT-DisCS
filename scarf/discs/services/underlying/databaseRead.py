import sys
sys.path.append('../../../')


from discs.settings import connect_with_database
from discs.data.underlying.users import User
from discs.data.underlying.posts import Post

import mongoengine

@connect_with_database
def get_user_by_id(pk, **kwargs):
    """
    Args: user id (primary key)
    Returns : User Object
    """
    user =  User.objects(id=pk).first()
    return user

@connect_with_database
def get_user_by_username(username, **kwargs):
    """
    Args:
        username 
    Returns:
        User Object
    """
    user = User.objects(username=username).first()
    return user

@connect_with_database
def readUsers(**kwargs):
    """
    Returns:
        Returns All Users Objects in a list
    """
    users =  User.objects()
    return users

@connect_with_database
def readPosts(**kwargs):
    """
    Returns:
        Returns All Posts Objects in a list
    """
    posts =  Post.objects()
    return posts

@connect_with_database
def get_post_by_id(post_pk, **kwargs):
    """
    Args:
        post_pk 
    Returns:
        Post Object
    """
    post = Post.objects(id=post_pk).first()
    return post

@connect_with_database
def get_posts_by_userid(user_pk, **kwargs):
    """
    Args:
        user_pk 
    Returns:
        List of Post_Ids
    """
    user = User.objects(id=user_pk).first()
    posts = user.posts
    # print("Posts : ", posts)
    return posts

@connect_with_database
def get_posts_by_username(username, **kwargs):
    """
    Returns post ids of posts made by a user.
    Args:
        username
    Returns:
        List of Post_Ids
    """
    user = User.objects(username=username).first()
    posts = user.posts
    return posts

@connect_with_database
def get_followers_by_userid(user_pk, **kwargs):
    """
    Returns list of follower usernames of a user.
    Args:
        user_pk
    Returns:
        List of Follower Usernames
    """
    user = User.objects(id=user_pk).first()
    return user.followers

@connect_with_database
def get_followers_by_username(username, **kwargs):
    """
    Returns list of follower usernames of a user.
    Args:
        username
    Returns:
        List of Follower Usernames
    """
    user = User.objects(username=username).first()
    return user.followers

@connect_with_database
def get_liked_posts_by_userid(user_pk, **kwargs):
    """
    Returns list of follower usernames of a user.
    Args:
        userid
    Returns:
        # List of Post_ids liked by the user
    """
    user = User.objects(id=user_pk).first()
    return user.liked_posts

@connect_with_database
def get_liked_posts_by_username(username, **kwargs):
    """
    Returns list of follower usernames of a user.
    Args:
        username
    Returns:
        # List of Post_ids liked by the user
    """
    user = User.objects(username=username).first()
    return user.liked_posts

@connect_with_database
def get_following_by_userid(user_pk, **kwargs):
    """
    Returns list of following usernames of a user.
    Args:
        userid
    Returns:
        # List of Following users
    """
    user = User.objects(id=user_pk).first()
    return user.followers

@connect_with_database
def get_following_by_username(username, **kwargs):
    """
    Returns list of following usernames of a user.
    Args:
        username
    Returns:
        # List of Following users
    """
    user = User.objects(username=username).first()
    return user.followers

@connect_with_database
def check_if_post_liked_by_userid(post_id, user_pk, **kwargs):
    user = User.objects(id=user_pk).first()
    liked_posts = user.liked_posts
    if post_id in liked_posts:
        return True
    else:
        return False

@connect_with_database
def check_if_post_liked_by_username(post_id, username, **kwargs):
    user = User.objects(username=username).first()
    liked_posts = user.liked_posts
    if post_id in liked_posts:
        return True
    else:
        return False

@connect_with_database
def get_number_of_likes_by_postid(post_id, **kwargs):
    post = Post.objects(id=post_id).first()
    likes = post.likes
    return likes
    

def print_posts(posts):
    """
    Function to print post objects
    
    Args:
        List of Post Objects
    """
    for post in posts:
        print_post(post)



def print_post(post):
    """
    Function to print a post object
    
    Args:
        Post Object
    """
    print('Post ID: ', post.id)
    print('Author: ', post.author)
    print('Creation Time: ', post.creation_time)
    print('Content: ', post.content)
    print('Likes: ', post.likes)
    print('\n')


def print_users(users):
    """
    Function to print user objects
    
    Args:
        List of User Objects
    """
    for user in users:
        print_user(user)


def print_user(user):
    """
    Function to print a user object
    
    Args:
        User Object
    """
    print('user_id: ', user.id)
    print('name: ', user.name)
    print('username: ', user.username)
    print('nationality: ', user.nationality)
    print('age: ', user.age)
    print('followers: ',user.followers)
    print('following: ', user.following)
    print('posts: ',user.posts)
    print('liked posts: ',user.liked_posts)
    print('\n')


if __name__ == "__main__":
    dbName = 'CRDT-DisCS_TEST_DB'
    mongoengine.register_connection(alias='core', name=dbName)
    
    import random
    from discs.manageDatabases import listDatabases, deleteDatabase
    from discs.services.underlying import databaseWrite
    from discs import populate


    deleteDatabase(dbName=dbName)
    
    print(listDatabases())

    populate.add_fake_users(40)
    populate.add_fake_posts(50)
    populate.add_random_likes(800)
    populate.add_random_followers(1000)
    
    users = readUsers()
    print_users(users)
    user = users[0]
    user_id = user.id
    username = user.username

    posts = readPosts()

    # databaseWrite.add_follower(users[0].username, users[1].username)
    

    # print("\nPosts : ", posts)

    post = posts[0]
    post_pk = post.id
    print_post(post)

    databaseWrite.add_post_likes(post_id=post_pk, username=user.username)

    print('---------------------- get_user_by_id --------------------')
    print_user(get_user_by_id(user_id))

    print('---------------------- get_user_by_username --------------------')
    print_user(get_user_by_username(username))

    print('---------------------- get_posts_by_userid --------------------')
    print(get_posts_by_userid(user_id))

    print('---------------------- get_post_by_id --------------------')
    print_post(get_post_by_id(post_pk))

    print('---------------------- get_posts_by_username --------------------')
    print(get_posts_by_username(username))

    print('---------------------- get_followers_by_userid --------------------')
    num_users = len(users)
    new_id = users[random.randint(0, num_users-1)].id
    followers = get_followers_by_userid(new_id)
    print(followers)

    print('---------------------- get_followers_by_username --------------------')
    num_users = len(users)
    new_username = users[random.randint(0, num_users-1)].username
    followers = get_followers_by_username(new_username)
    print(followers)

    print('---------------------- get_liked_posts_by_userid --------------------')
    liked_posts = get_liked_posts_by_userid(user_id)
    print(liked_posts)

    print('---------------------- get_liked_posts_by_username --------------------')
    liked_posts = get_liked_posts_by_username(username)
    print(liked_posts)
    
    print('---------------------- get_following_by_userid --------------------')
    num_users = len(users)
    new_id = users[random.randint(0, num_users-1)].id
    following = get_following_by_userid(new_id)
    print(following)

    print('---------------------- get_following_by_username --------------------')
    num_users = len(users)
    new_username = users[random.randint(0, num_users-1)].username
    following = get_following_by_username(new_username)
    print(following)

    print('---------------------- check_if_post_liked_by_userid --------------------')
    print(check_if_post_liked_by_userid(post_pk, user_id))


    print('---------------------- check_if_post_liked_by_username --------------------')
    print(check_if_post_liked_by_username(post_pk, username))

    print('---------------------- get_num_likes_by_post_id --------------------')
    new_post_index = random.randint(0, len(posts)-1)
    new_post_pk = posts[new_post_index].id
    print(get_number_of_likes_by_postid(new_post_pk))

    deleteDatabase(dbName=dbName)
    
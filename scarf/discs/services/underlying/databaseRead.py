from discs.settings import connect_with_database
from discs.data.underlying.users import User
from discs.data.underlying.posts import Post

import mongoengine

@connect_with_database
def readUser(user_id, **kwargs):
    user =  User.objects(user_id=user_id).first()
    return user


@connect_with_database
def readUsers(**kwargs):
    users =  User.objects()
    return users

@connect_with_database
def readPosts(**kwargs):
    posts =  Post.objects()
    return posts


def print_posts(posts):
    for post in posts:
        print_post(post)



def print_post(post):
    print('Post ID: ', post.id)
    print('Author: ', post.author)
    print('Creation Time: ', post.creation_time)
    print('Content: ', post.content)
    print('Likes: ', post.likes)
    print('\n')


def print_users(users):
    for user in users:
        print_user(user)


def print_user(user):
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
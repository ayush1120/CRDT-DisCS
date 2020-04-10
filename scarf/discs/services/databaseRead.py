from discs.settings import connect_with_database
from discs.data.users import User

import mongoengine

@connect_with_database
def readUser(user_id, **kwargs):
    user =  User.objects(user_id=user_id).first()
    return user


@connect_with_database
def readUsers(**kwargs):
    users =  User.objects()
    return users


def print_users(users):
    for user in users:
        print_user(user)
        print('\n')


def print_user(user):
    print('user_id: ', user.user_id)
    print('name: ', user.name)
    print('age: ', user.age)
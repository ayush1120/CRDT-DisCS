import sys
import os
sys.path.append('../../../')

from discs.data.underlying.posts import Post
from discs.data.underlying.users import User

from discs.manageDatabases import listDatabases, deleteDatabase
from discs.settings import connect_with_database


DB_NAME = 'My_Test_Database_CRDT-DisCS'


@connect_with_database
def add_user(name='Ayush Sharma', username='aush', nationality='Indian', age=20, **kwargs):
    user = User()
    user.full_name = name
    user.username = username
    user.nationality = nationality
    user.age = age
    user.save()

@connect_with_database
def readUsers(**kwargs):
    users =  User.objects()
    return users

if __name__ == "__main__":
    print(listDatabases())
    add_user(username='snew_user', age=45, dbName=DB_NAME)
    users = readUsers(dbName=DB_NAME)
    print(users)
    print(users[0].name)
    print(users[0].username)
    print(users[0].age)
    print(users[0].nationality)
    print(users[0].followers)
    print(users[0].following)

    print(listDatabases())
    deleteDatabase(dbName=DB_NAME)
    print(listDatabases())

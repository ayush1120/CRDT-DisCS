import sys
import os
sys.path.append('../../../')

from discs.data.middleware.users_update import Users_update
from discs.data.underlying.users import User

from discs.manageDatabases import listDatabases, deleteDatabase
from discs.settings import connect_with_middleware_database

DB_NAME = 'My_Test_Database_CRDT-DisCS'

@connect_with_middleware_database
def update_users(data='Ayush Sharma', **kwargs):
    user = Users_update()
    user.users = data
    user.save()

@connect_with_middleware_database
def readUsers(**kwargs):
    users =  Users_update.objects()
    return users

if __name__ == "__main__":
    print(listDatabases())
    update_users(data='snew_user', dbName=DB_NAME)
    users = readUsers(dbName=DB_NAME)
    for i in users:
        print(i.users)
    update_users(dbName=DB_NAME)
    print(users[1].users)
    
    print(listDatabases())
    deleteDatabase(dbName=DB_NAME)
    print(listDatabases())


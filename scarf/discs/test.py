import sys
sys.path.append('..')
import mongoengine
from discs.data.users import User
from services import databaseWrite
from services.databaseWrite import connect_with_database
from manageDatabases import listDatabases, deleteDatabase
from discs.services.databaseRead import *

def global_init():
    mongoengine.register_connection(alias='core', name='test_db')



def main():
    global_init()

    # user = databaseWrite.addUser('13', 'Ram', 34, 'Indian')
    curr_id =  '13'
    curr_user = readUsers(curr_id)
    # print_user(curr_user)
    if not curr_user:
        print("Already Deleted")
    else:
        print_user(curr_user)
        databaseWrite.deleteUser(curr_id)
        print("User Deleted")


if __name__ == "__main__":
    # main()
    print("Before Running the Code :" ,listDatabases())
    deleteDatabase(dbName='CRDT-DisCS__DB1')
    deleteDatabase(dbName='CRDT-DisCS__DB2')
    print(listDatabases())
    databaseWrite.addUser("newUser", "Shyam", 34, "Indian", dbName="CRDT-DisCS__DB1")
    databaseWrite.addUser("newUser1", "Rohith", 32, "Pakistani", dbName="CRDT-DisCS__DB2")
    databaseWrite.addUser("newUser2", "Jose", 30, "African", dbName="CRDT-DisCS__DB2")
    print(listDatabases())
    print("In database CRDT-DisCS__DB1 : ")
    users = readUsers(dbName='CRDT-DisCS__DB1')
    print_users(users)
    print("In database CRDT-DisCS__DB2 : ")
    users = readUsers(dbName='CRDT-DisCS__DB2')
    print_users(users)
    print(listDatabases())
    deleteDatabase(dbName='CRDT-DisCS__DB1')
    deleteDatabase(dbName='CRDT-DisCS__DB2')
    print(listDatabases())
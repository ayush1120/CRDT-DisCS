import sys
sys.path.append('..')
import mongoengine
from discs.data.underlying.users import User
from discs.services.underlying import databaseWrite
from discs.settings import connect_with_database
from discs.manageDatabases import listDatabases, deleteDatabase, delete_project_databases
from discs.services.underlying.databaseRead import *



if __name__ == "__main__":
    print("Before Running the Code :" ,listDatabases())
    deleteDatabase(dbName='CRDT-DisCS__DB1')
    deleteDatabase(dbName='CRDT-DisCS__DB2')
    print(listDatabases())
    databaseWrite.add_user("Shyam", "newUser",  "Indian",     34, dbName="CRDT-DisCS__DB1")
    databaseWrite.add_user("Rohith", "newUser1", "Pakistani", 32, dbName="CRDT-DisCS__DB2")
    databaseWrite.add_user("Jose",   "newUser2", "African",   30, dbName="CRDT-DisCS__DB2")
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
    
                
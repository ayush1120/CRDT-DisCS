import sys
sys.path.append('../scarf')

from discs.services.underlying import databaseRead
from discs.manageDatabases import deleteDatabase

import mongoengine
from num_running_servers import NUM_SERVERS

dbNames = ['RAFT_DB_' + str(i) for i in range(0,3)]

def test_changes_in dbs(NUM_SERVERS=NUM_SERVERS):
    dbNames = ['RAFT_DB_' + str(i) for i in range(0,NUM_SERVERS)]
    for dbName in dbNames:
        mongoengine.register_connection(alias='core', name=dbName)
        users = databaseRead.readUsers(dbName=dbName)
        print("Database Name : ", dbName)
        print("Num of Users : ", len(users))
        print('----------Users------------')
        databaseRead.print_users(users)
        mongoengine.disconnect(alias='core')


if __name__ == "__main__":
    for dbName in dbNames:
        users = databaseRead.readUsers(dbName=dbName)
        print("Database Name : ", dbName)
        print("Num of Users : ", len(users))
        # databaseRead.print_users(users)
        deleteDatabase(dbName)
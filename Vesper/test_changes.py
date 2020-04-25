import sys
sys.path.append('../scarf')

from discs.services.underlying import databaseRead
from discs.manageDatabases import deleteDatabase



dbNames = ['RAFT_DB_' + str(i) for i in range(0,3)]


if __name__ == "__main__":
    for dbName in dbNames:
        users = databaseRead.readUsers(dbName=dbName)
        print("Database Name : ", dbName)
        print("Num of Users : ", len(users))
        # databaseRead.print_users(users)
        deleteDatabase(dbName)
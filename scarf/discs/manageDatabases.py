import pymongo
import time

def getClient():
    client = pymongo.MongoClient()
    return client


def listDatabases(client=None):
    if not client:
        client = pymongo.MongoClient()
    dbNames = client.list_database_names()
    return dbNames


def ifDatabaseExists(dbName, client=None):
    dbNames = listDatabases(client=client)
    if dbName in dbNames:
        return True
    return False


def createDatabase(dbName, client=None):
    if not client:
        client = pymongo.MongoClient()

    createdDatabase = client[dbName]
    return createdDatabase

def deleteDatabase(dbName, client=None):
    if not client:
        client = pymongo.MongoClient()
    client.drop_database(dbName)


if __name__ == "__main__":
    print(listDatabases())
    numDatabases = 4
    for i in range(1, numDatabases+1):
        dbName = "CRDT-DisCS__DB"+str(i)
        mydb = createDatabase(dbName=dbName)
        mycol = mydb["customers"]
        mydict = { "name": "John", "address": "Highway 37" }
        x = mycol.insert_one(mydict)

    print(listDatabases())
    for i in range(1, numDatabases+1):
        dbName = "CRDT-DisCS__DB"+str(i)
        deleteDatabase(dbName=dbName)
    print(listDatabases())
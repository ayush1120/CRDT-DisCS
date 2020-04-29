import sys
sys.path.append('../../')

import mongoengine
from discs import  manageDatabases

class Node:


    def __init__(self, index, deleteOldDatabases=False):
        self.middlewareDB = 'CRDT-DisCS_Node_Middleware_' + str(index)
        self.coreDB       = 'CRDT-DisCS_Node_Core_'       + str(index)

        if deleteOldDatabases:
            manageDatabases.deleteDatabase(dbName=self.coreDB)
            manageDatabases.deleteDatabase(dbName=self.middlewareDB)


        mongoengine.register_connection()


import sys
sys.path.append('../../')

import mongoengine
import logging
import asyncio

from discs import manageDatabases

from crdt.server.config import NUM_SERVERS

class Node:

    NUM_SERVERS = NUM_SERVERS

    def __init__(self, index, deleteOldDatabases=False, host='0.0.0.0', port=6000):
        self.index = index

        # Logging
        logging.basicConfig(filename=f'node{self.index}.log', 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
        logger = logging.getLogger('CRDT Logger')
        logger.setLevel(logging.DEBUG)
        logger.debug(f'Node {self.index} Initialized.')


        self.host = host
        self.port = port + int(self.index)
        self.server_address = f'http://{self.host}:{str(self.port)}'
        
        self.other_adresses = self.get_other_addresses()
        
        
        self.middlewareDB = 'CRDT-DisCS_Node_Middleware_' + str(index)
        self.coreDB       = 'CRDT-DisCS_Node_Core_'       + str(index)

        self.loop = asyncio.get_event_loop()


        if deleteOldDatabases:
            manageDatabases.deleteDatabase(dbName=self.coreDB)
            manageDatabases.deleteDatabase(dbName=self.middlewareDB)

        # mongoengine.register_connection(alias='core', name=self.coreDB)
        # mongoengine.register_connection(alias='middle', name=self.middlewareDB)


        print('Server Node Established.')
        print(f'Connected to {self.coreDB}.')
        print(f'Connected to {self.middlewareDB}.')


    def get_other_addresses(self):
        other_indices = []
        port = self.port - self.index
        for i in range(1, NUM_SERVERS+1):
            if i!=self.index:
                other_indices.append(i)
        other_addresses = [ f'http://{self.host}:{str(port+i)}' for i in other_indices ]
        return other_addresses 
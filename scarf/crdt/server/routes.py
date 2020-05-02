import sys
sys.path.append('../../')
from flask import Flask, jsonify, request
import time
import os, signal
import json
import logging

from crdt.server.server import app
import pymongo
from discs.manageDatabases import deleteDatabase

logger = logging.getLogger('CRDT Logger')


def hello(serverNode):
    logger.debug(f'Hello function Called at ServerNode {serverNode.index}')
    output =  {
        "output" : "Hello World",
        "recieved_messege": request.json
    }
    output = 'hmmmmmm'
    return jsonify(output)

def parse_messege(serverNode, sender_index, messege):
    deleteDatabase(serverNode.coreDB)
    deleteDatabase(serverNode.middlewareDB)
    client = pymongo.MongoClient()
    source = 'CRDT-DisCS_Node_Middleware_'+str(sender_index)
    dst = 'CRDT-DisCS_Node_Middleware_' + str(serverNode.index)
    client.admin.command('copydb',
                         fromdb=source,
                         todb=dst)
    source = 'CRDT-DisCS_Node_Core_' + str(sender_index)
    dst = 'CRDT-DisCS_Node_Core_' + str(serverNode.index)
    client.admin.command('copydb',
                         fromdb=source,
                         todb=dst)
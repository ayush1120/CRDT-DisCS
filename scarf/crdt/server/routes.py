import sys
sys.path.append('../../')
from flask import Flask, jsonify, request
import time
import os, signal
import json
import logging

from crdt.server.server import app


logger = logging.getLogger('CRDT Logger')


def hello(serverNode):
    logger.debug(f'Hello function Called at ServerNode {serverNode.index}')
    output =  {
        "output" : "Hello World",
        "recieved_messege": request.json
    }
    return jsonify(output)


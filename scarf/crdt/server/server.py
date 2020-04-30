from flask import Flask, jsonify, request
import time
import os, signal
import json
import logging
import sys
sys.path.append('../../')

from crdt.server.node import Node
from crdt.server.config import NUM_SERVERS

app = Flask(__name__)


from crdt.server import routes 


@app.route('/stopServer', methods=['GET'])
def stopServer():
    logger.debug('Server Shutdown Initiated')
    os.kill(os.getpid(), signal.SIGINT)
    logger.debug(f'ServerNode {serverNode.index} is shutting down.')
    return jsonify({ "success": True, "message": "Server is shutting down..." })


@app.route("/sendRequest", methods=['GET'])
def hello():
    return routes.hello(serverNode)

@app.route('/sendMessage', methods=['POST'])
def sendDataToAll(data, index):
    message = {
        'sender_index' : serverNode.index,
        'sender_address': serverNode.server_address,
        'data' : data
    }



@app.route('/sendMessage', methods=['POST'])
def sendAck(message, index):
    pass



def startServer(index=1, port=6000, host='0.0.0.0'):
    global app
    global logger
    global serverNode
    if (index<0 or index>NUM_SERVERS):
        print('Wrong Serber Index Provided. Please Check config.')
        return

    serverNode = Node(index, deleteOldDatabases=True, host=host, port=port)
    logger = logging.getLogger('CRDT Logger')
    app.run(host=serverNode.host, port=serverNode.port)


if __name__ == "__main__":
    global logger
    serverNode = Node(index, deleteOldDatabases=True)
    logger = logging.getLogger('CRDT Logger')
    app.run(host='0.0.0.0', port=port)
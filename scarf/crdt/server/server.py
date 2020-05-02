from flask import Flask, jsonify, request
import time
import os, signal
import json
import logging
import concurrent.futures
import sys
import requests
sys.path.append('../../')



from crdt.server.node import Node
from crdt.server.config import NUM_SERVERS

app = Flask(__name__)


from crdt.server import routes
from crdt.server.routes import parse_messege 


@app.route('/stopServer', methods=['GET'])
def stopServer():
    logger.debug('Server Shutdown Initiated')
    
    serverNode.loop.stop()
    os.kill(os.getpid(), signal.SIGINT)
    
    logger.debug(f'ServerNode {serverNode.index} is shutting down.')
    
    return jsonify({ "success": True, "message": "Server is shutting down..." })


@app.route("/sendRequest", methods=['GET'])
def hello():
    return routes.hello(serverNode)



@app.route("/testSending", methods=['GET'])
def test_sending():
    message = request.json
    start_time = time.perf_counter()
    logger.debug('This was executed')
    response = sendDataToAll(message)
    logger.debug('Consensus was reached')
    finish_time = time.perf_counter()
    out_string = f'Completed in {round(finish_time-start_time, 3)} seconds...'
    return jsonify(out_string) 


@app.route("/recieveData", methods=['GET'])
def recieveData():
    message = request.json
    logger.debug(f'Recieved Message from Node {message["sender_index"]}')
    logger.debug(f'Data :  {message["data"]}')
    sender_index = message["sender_index"]
    parse_messege(serverNode, sender_index, message)
    output = 'OK'
    return jsonify(output)
    


def sendMessage(server_address, message):
    logger.debug(f'Sending to {server_address}')
    while True:
        try:
            response = requests.get(server_address, json=message)
            logger.debug(f'Got Response from {server_address}')
            logger.debug(f'Response : {response.json()}')
            break
        except Exception as e:
            logger.debug(f'Exception Occured : {e}')
            return None
            


    return response.json



def sendDataToAll(data):
    other_addresses = serverNode.other_adresses
    message = {
        'sender_index' : serverNode.index,
        'sender_address': serverNode.server_address,
        'data' : data
    }

    for address in other_addresses:
        address = address + '/recieveData'
        response = sendMessage(address, message)

    output = 'OK'
    return output

        




@app.route('/sendMessage', methods=['POST'])
def sendAck(message, index):
    return jsonify('lol')



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
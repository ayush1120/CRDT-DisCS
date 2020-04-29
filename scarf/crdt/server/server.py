from flask import Flask, jsonify, request
import time
import os, signal
import json

app = Flask(__name__)



@app.route("/sendRequest", methods=['GET'])
def hello():
    output =  {
        "output" : "Hello World",
        "recieved_messege": request.json
    }
    return jsonify(output)

@app.route('/stopServer', methods=['GET'])
def stopServer():
    print('lol')
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
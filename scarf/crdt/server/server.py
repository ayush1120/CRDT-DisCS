from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    output =  {
        "output" : "Hello World"
    }
    return jsonify(output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
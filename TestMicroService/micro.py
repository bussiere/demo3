from flask import Flask
from flask import jsonify
app = Flask(__name__)
from functools import wraps
from flask import request, current_app
from flask.ext.jsonpify import jsonify




@app.route("/")
def hello():
    data = {}
    data[0] = "Hello World!"
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

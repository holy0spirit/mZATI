from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def helloworld():

    return jsonify({"message" : "Hello World", "status" : "200"})
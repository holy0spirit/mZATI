# from crypt import methods
from flask import Flask, jsonify, request
import string
import random
import json
from cryptography.fernet import Fernet
from anchor.generate import Generate
from model.json import JSON

app = Flask(__name__)

@app.route('/')
def helloworld():

    return jsonify({"message" : "Hello World", "status" : "200"})


@app.route('/gen', methods=["GET"])
def mJsonGenerate():

    mGen = Generate.mGenerate()

    return jsonify(mGen)
    

@app.route('/post_json', methods=["GET"])
def mJSONPostData():

    mPostData = JSON.mPostData(request)

    return jsonify(mPostData)
    



@app.route('/get_json', methods=["GET"])
def mJSONGetData():
    
    mGetData = JSON.mGetData(request)
    
    return jsonify(mGetData)
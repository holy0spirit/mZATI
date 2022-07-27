# from crypt import methods
from flask import Flask, jsonify, request, render_template
import string
import random
import json
from cryptography.fernet import Fernet
from anchor.generate import Generate
from model.json import JSON
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def onSite():

    return render_template("index.html")


@app.route('/gen', methods=["GET"])
def mJsonGenerate():

    mGen = Generate.mGenerate()

    return jsonify(mGen)
    

@app.route('/post_json', methods=["POST"])
def mJSONPostData():

    mPostData = JSON.mPostData(request)

    return jsonify(mPostData)
    

@app.route('/get_json', methods=["POST"])
def mJSONGetData():
    
    mGetData = JSON.mGetData(request)
    
    return jsonify(mGetData)
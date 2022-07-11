# from crypt import methods
from flask import Flask, jsonify, request
import string
import random
import json
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def helloworld():

    return jsonify({"message" : "Hello World", "status" : "200"})

@app.route('/gen', methods=["GET"])
def mJsonGenerate():
    mFileName = mFileNameGenerator()
    mJsonFile = open("%s.txt" % mFileName, "w")

    return jsonify({"message" : "Successful. Key generated.", "status" : "200", "key" : mFileName})

@app.route('/post_json', methods=["POST"])
def mJSONPostData():
    # get post data
    mPostData = request.get_json()
    mFileName = mPostData["key"]
    mData = mPostData["data"][0]

    
    mEncryptionKey = mJSONDataEncryptionKey(mFileName)

    # convert json to bytes
    mJSONDataBytes = json.dumps(mData).encode('utf-8')

    # # encrypt json data
    mEncryptor = Fernet(mEncryptionKey)
    mEncryptedData = mEncryptor.encrypt(mJSONDataBytes)

    # conver encrypted data to string
    mEncryptedDataString = mEncryptedData.decode("utf-8")
    

    # # store encrypted data
    mJsonFile = open("%s.txt" % mFileName, "w")
    mJsonFile.write(mEncryptedDataString)
    mJsonFile.close()

    
    return jsonify({"message" : "Successful. Post JSON data.", "status" : "200", "key" : mFileName})

@app.route('/get_json', methods=["POST"])
def mJSONGetData():
    # get post data
    mPostData = request.get_json()
    mFileName = mPostData["key"]
    mFileExist = mCheckFileExist(mFileName)
    mFile = mCheckFileNotEmpty(mFileExist)
    # print(mFile)

    # get decryptor key
    mMessage = mDecryptor(mFileName, mFile)
    mJSONMessage = json.loads(mMessage)

    # if len(mKeys) > None:
    #     return jsonify({"message" : "Unsuccessful. Invalid Key", "status" : "405"})
    # else:
    #     mDecryptor = mCrackFile(mKeys, mFile)
    

    
    return jsonify({"message" : "Successful. Get JSON data.", "status" : "200", "key" : mFileName, "data" : mJSONMessage})

def mFileNameGenerator(size=11, chars=string.ascii_uppercase + string.digits):
    mFileName = ''.join(random.choice(chars) for _ in range(size))
    return mFileName

def mJSONDataEncryptionKey(mFileName):
    mEncryptionkey = Fernet.generate_key()
    mEcryptionString = mEncryptionkey.decode("utf-8")
    mKeyData = '{"%s" : "%s"},' % (mFileName, mEcryptionString)
    with open('key.json','a') as file:
        file.write(mKeyData)

    return mEncryptionkey

def mCheckFileExist(mFileName):
    try:
        mFile = open("%s.txt" % mFileName, "r")
        if mFile is not None:
            return mFile
    except:
        print("Something went wrong")

def mCheckFileNotEmpty(mFile):
    try:
        mFileToCheck = mFile.read()
        if len(mFileToCheck) > 0 :
            
            return mFileToCheck
    except:
        print("Something went wrong")

def mDecryptor(mFileName, mFile):
    with open('key.json','r') as file:
        mKeyFile = file.read()
        file.close()

    mRows = mKeyFile.split(",")

    for mRow in mRows:
        if mFileName in mRow:
            mJSONData = json.loads(mRow)
            mKey = mJSONData[mFileName]
            mKeyByte = bytes(mKey, 'utf-8')
            mFileByte = bytes(mFile, 'utf-8')
            # print(mFileByte)
            
            # decrypt
            mDecryptor = Fernet(mKeyByte)
            mDeciferMessage = mDecryptor.decrypt(mFileByte)

            # return decifer message in json
            mMessageString = mDeciferMessage.decode("utf-8")
            return mMessageString

            
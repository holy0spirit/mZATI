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
    try:
        # generate key
        mFileName = mFileNameGenerator()

        # create file
        mJsonFile = open("%s.txt" % mFileName, "w")

        # create HashKey
        mJSONDataEncryptionKey(mFileName)

        return jsonify({"message" : "Successful. Key generated.", "status" : "200", "key" : mFileName})
    except Exception as e:
        return jsonify({"message" : "Error M201. " + str(e), "status" : "501"})

@app.route('/post_json', methods=["GET"])
def mJSONPostData():
    try:
        # get post data
        mPostData = request.get_json()
        mFileName = mPostData["key"]
        mData = mPostData["data"][0]

        # get encryption key
        mEncryptionKey = mHashKey(mFileName)

        # convert json to bytes
        mJSONDataBytes = json.dumps(mData).encode('utf-8')

        # encrypt json data
        mEncryptor = Fernet(mEncryptionKey)
        mEncryptedData = mEncryptor.encrypt(mJSONDataBytes)

        # convert encrypted data to string
        mEncryptedDataString = mEncryptedData.decode("utf-8")

        # store encrypted data
        mStoreJSONData(mFileName, mEncryptedDataString)

        return jsonify({"message" : "Successful. Post JSON data.", "status" : "200", "key" : mFileName})
    except Exception as e:
        return jsonify({"message" : "Error M200. " + str(e), "status" : "501"})

# Function to store JSON data
def mStoreJSONData(mFileName, mEncryptedDataString):
    try:
        # create file
        mJsonFile = open("%s.txt" % mFileName, "a")
        # write data to file
        mJsonFile.write("," + mEncryptedDataString)
        # close file
        mJsonFile.close()
    except Exception as e:
        return jsonify({"message" : "Error M100. " + str(e), "status" : "501"})

@app.route('/get_json', methods=["GET"])
def mJSONGetData():
    try:
        # get post data
        mPostData = request.get_json()
        mFileName = mPostData["key"]

        # check for file
        mFileExist = mCheckFileExist(mFileName)
        mFile = mCheckFileNotEmpty(mFileExist)
        # print(mFile)

        # get decryptor key
        mData = mDecryptor(mFileName, mFile)
        
        return jsonify({"message" : "Successful. Get JSON data.", "status" : "200", "key" : mFileName, "data" : mData})
    except Exception as e:
        return jsonify({"message" : "Error M202. " + str(e), "status" : "501"})

def mFileNameGenerator(size=11, chars=string.ascii_uppercase + string.digits):
    try:
        # generate key
        mFileName = ''.join(random.choice(chars) for _ in range(size))
        return mFileName
    except Exception as e:
        return jsonify({"message" : "Error M101. " + str(e), "status" : "501"})

def mJSONDataEncryptionKey(mFileName):
    try:
        # generate hash key     
        mEncryptionkey = Fernet.generate_key()
        # convert hash key to string
        mEcryptionString = mEncryptionkey.decode("utf-8")
        # key value pair
        mKeyData = '{"%s" : "%s"},' % (mFileName, mEcryptionString)
        # create and write key.json
        with open('key.json','a') as file:
            file.write(mKeyData)

        return mEncryptionkey
    except Exception as e:
        return jsonify({"message" : "Error M102. " + str(e), "status" : "501"})

def mCheckFileExist(mFileName):
    try:
        # open file
        mFile = open("%s.txt" % mFileName, "r")
        # check for file
        if mFile is not None:
            return mFile
    except Exception as e:
        return jsonify({"message" : "Error M103. " + str(e), "status" : "501"})

def mCheckFileNotEmpty(mFile):
    try:
        # read file
        mFileToCheck = mFile.read()
        # check if not empty
        if len(mFileToCheck) > 0 :
            
            return mFileToCheck
    except Exception as e:
        return jsonify({"message" : "Error M104. " + str(e), "status" : "501"})

def mHashKey(mFileName):
    try:
        # open file
        with open('key.json','r') as file:
            # read file
            mKeyFile = file.read()
            # close file
            file.close()
        # convert to list
        mRows = mKeyFile.split(",")

        # forloop
        for mRow in mRows:
            if mFileName in mRow:
                # convert to json
                mJSONData = json.loads(mRow)
                # get hash key
                mKey = mJSONData[mFileName]
                # convert to bytes
                mKeyByte = bytes(mKey, 'utf-8')

                return mKeyByte
    except Exception as e:
        return jsonify({"message" : "Error M105. " + str(e), "status" : "501"})


def mDecryptor(mFileName, mFile):
    try:
        # get hash key
        mKey = mHashKey(mFileName)
        # convert to list
        mFiles = mFile.split(",")
        # create data array
        mData = []
        # forloop
        for mF in mFiles:
            # check if it's not empty
            if len(mF) > 0 :
                # convert to bytes
                mFileByte = bytes(mF, 'utf-8')
                # decrypt
                mDecryptor = Fernet(mKey)
                mDeciferMessage = mDecryptor.decrypt(mFileByte)
                # convert to string
                mMessageString = mDeciferMessage.decode("utf-8")
                # conver to json obj
                mJSONMessage = json.loads(mMessageString)
                # add to list
                mData.append(mJSONMessage)


        return mData
    except Exception as e:
        return jsonify({"message" : "Error M106. " + str(e), "status" : "501"})
    


            
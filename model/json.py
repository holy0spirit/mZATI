import json
from components.hash import Hash
from anchor.storage import Storage
from components.file import File
from components.cipher import Cipher
from cryptography.fernet import Fernet

class JSON:
    def mPostData(request):
        try:
            # get post data
            mPostData = request.get_json()
            mFileName = mPostData["key"]
            mData = mPostData["data"]

            # DEMO TEST DATA
            # mFileName = 'PWP7O6ML3YN'
            # mData = {
            #     "name" : "Abe Duke",
            #     "gender" : "female",
            #     "age" : "16"
            # }

            # get encryption key
            mEncryptionKey = Hash.mHash(mFileName)

            # convert json to bytes
            mJSONDataBytes = json.dumps(mData).encode('utf-8')

            print(mEncryptionKey)

            # encrypt json data
            mEncryptor = Fernet(mEncryptionKey)
            

            mEncryptedData = mEncryptor.encrypt(mJSONDataBytes)

          

            # convert encrypted data to string
            mEncryptedDataString = mEncryptedData.decode("utf-8")
            

            # store encrypted data
            Storage.mStorage(mFileName, mEncryptedDataString)
            

            return {"message" : "Successful. Post JSON data.", "status" : "200", "key" : mFileName}
        except Exception as e:
            return {"message" : "Error M200. " + str(e), "status" : "501"}

    def mGetData(request):
        try:
            # get post data
            mPostData = request.get_json()
            mFileName = mPostData["key"]

            # # DEMO TEST DATA
            # mFileName = 'PWP7O6ML3YN'

            # check for file
            mFileExist = File.mCheckFileExist(mFileName)
            mFile = File.mCheckFileNotEmpty(mFileExist)

            # get decryptor key
            mData = Cipher.mDecryptor(mFileName, mFile)
            
            return {"message" : "Successful. Get JSON data.", "status" : "200", "key" : mFileName, "data" : mData}
        except Exception as e:
            return {"message" : "Error M202. " + str(e), "status" : "501"}
from cryptography.fernet import Fernet
from components.hash import Hash
import json

class Cipher:
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
            return {"message" : "Error M102. " + str(e), "status" : "501"}
    
    def mDecryptor(mFileName, mFile):
        try:
            # get hash key
            mKey = Hash.mHash(mFileName)
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
            return {"message" : "Error M106. " + str(e), "status" : "501"}
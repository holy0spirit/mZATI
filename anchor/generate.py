from importlib import import_module
from components.file import File
from components.cipher import Cipher
class Generate:
    def mGenerate():
        try:
            # generate key
            mFileName = File.mFileNameGenerator()

            # create file
            mJsonFile = open("storage/%s.txt" % mFileName, "w")

            # create HashKey
            mHashKey = Cipher.mJSONDataEncryptionKey(mFileName)
            print(mHashKey)

            return {"message" : "Successful. Key generated.", "status" : "200", "key" : mFileName}
        except Exception as e:
            return {"message" : "Error M201. " + str(e), "status" : "501"}
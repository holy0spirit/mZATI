import string
import random
class File:
    def mFileNameGenerator(size=11, chars=string.ascii_uppercase + string.digits):
        try:
            # generate key
            mFileName = ''.join(random.choice(chars) for _ in range(size))
            return mFileName
        except Exception as e:
            return {"message" : "Error M101. " + str(e), "status" : "501"}
    
    def mCheckFileExist(mFileName):
        try:
            # open file
            mFile = open("storage/%s.txt" % mFileName, "r")
            # check for file
            if mFile is not None:
                return mFile
        except Exception as e:
            return {"message" : "Error M103. " + str(e), "status" : "501"}

    def mCheckFileNotEmpty(mFile):
        try:
            # read file
            mFileToCheck = mFile.read()
            # check if not empty
            if len(mFileToCheck) > 0 :
                
                return mFileToCheck
        except Exception as e:
            return {"message" : "Error M104. " + str(e), "status" : "501"}
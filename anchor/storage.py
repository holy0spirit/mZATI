class Storage:
    def mStorage(mFileName, mEncryptedDataString):
        try:
            # create file
            mJsonFile = open("storage/%s.txt" % mFileName, "a")
            # write data to file
            mJsonFile.write("," + mEncryptedDataString)
            # close file
            mJsonFile.close()
        except Exception as e:
            return {"message" : "Error M100. " + str(e), "status" : "501"}
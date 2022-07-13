import json

class Hash:
    def mHash(mFileName):
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
            return {"message" : "Error M105. " + str(e), "status" : "501"}

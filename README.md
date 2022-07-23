# mZATI
 ###### JSON Encrypted Data Storage for Developers

 > Working with JSON Data? You have the best JSON Database here fully encrypted for your privacy.

 ###### Try it out.

 ## Generate Key

 Send a GET request to https://swaqdb.herokuapp.com/gen

###### Python
 ```
    import requests

    url = "https://swaqdb.herokuapp.com/gen"

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
```

## POST JSON Object to Storage

Add the key to your root-node

###### JSON SCHEMA

```
    {
        "key" : "XXXXXXXXXXX",
        "data" : [
    {
        "name" : "Ulande Victoria",
        "age" : "17",
        "gender" : "female",
        "email" : "ulande.victoria@aol.com",
        "phone" : "08000000000"
    },
    {
        "name" : "Ulande Victoria",
        "age" : "17",
        "gender" : "female",
        "email" : "ulande.victoria@aol.com",
        "phone" : "08000000000"
    },
    {
        "name" : "Ulande Victoria",
        "age" : "17",
        "gender" : "female",
        "email" : "ulande.victoria@aol.com",
        "phone" : "08000000000"
    }
        ]
        
    }
```

Send a POST request to https://swaqdb.herokuapp.com/post_json

###### Python
```
    import requests
    import json

    url = "https://swaqdb.herokuapp.com/post_json"

    payload = json.dumps({
    "key": "XXXXXXXXXXX",
    "data": json-data
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
```

## Get JSON Object from Storage

Retrieve your JSON Object from storage using your key

###### Python
```
    import requests
    import json

    url = "https://swaqdb.herokuapp.com/get_json"

    payload = json.dumps({
    "key": "XXXXXXXXXXX"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
```



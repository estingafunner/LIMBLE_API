import time
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode
from json import dumps, loads
from pprint import pprint
import numpy as np



def update_FC(coolshit): #THIS SHOULD BE THE LAST STEP - sending the API/Update with new Priority Levels
    print(coolshit)
    PRIid = 1
    taskID = 59


    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = json.dumps({
        "priority": PRIid
    })
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'Content-Type': 'application/json'
    }
    
    ###TaskID will go HERE!
    conn.request("PATCH", "/v2/tasks/59", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    print("THIS IS THE END OF THIS THING")

    return()

update_FC("THis")
import time
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode
from json import dumps, loads
from pprint import pprint
#import numpy as np


def update_FC(): #THIS SHOULD BE THE LAST STEP - sending the API/Update with new Priority Levels
    coolshit = 0
    PRIid = 5
    taskID = 59


    conn = http.client.HTTPSConnection("")
    payload = json.dumps({
        "priority": PRIid
    })
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'assetID': '',
        'Content-Type': json
    }
    
    ###TaskID will go HERE!
    conn.request("PATCH", "//api.limblecmms.com:443/v2/tasks/"+ str(taskID), payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


    return(print(coolshit))
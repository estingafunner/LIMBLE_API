#INTEGRATES with ApiPython002.py AND ApiPython003-1.py
import time
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode
from json import dumps, loads
from pprint import pprint


def update_FC(notSurYet):
    coolshit = 0
    conn = http.client.HTTPSConnection("")
    payload = json.dumps({
        "name": "Do this task please!",
        "locationID": 163,
        "assetID": 1,
        "due": 1564605614,
        "type": 6,
        "assignment": 341,
        "assignmentType": "user",
        "priority": 3,
        "description": "this is a test task",
        "requestName": "requtest name",
        "requestEmail": "requestemail@domain.com",
        "requestPhone": "1111111111",
        "requestDescription": "request description",
        "status": 1,
        "meta1": "meta1",
        "meta2": "meta2",
        "meta3": "meta3"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic e3thcGlVTn19Ont7YXBpUGFzc319'
    }
    conn.request("PATCH", "//api.limblecmms.com:443/v2/tasks/",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    """      conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization' : 'Basic %s' %  userAndPass,
        'assetID': ''
    }
    conn.request("GET", "/v2/tasks/?limit=" + str(limited) + "&status=0", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)
        """
    return int(coolshit)

def calc_filterCode(risk, sev, pdc):
    bigFC = int(risk) * int(sev) * int(pdc)
    #bigFC = 777
    return int(bigFC)

def find_risk(etID):
    #print(etID)
    riskOut = 0
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'assetID': ''
    }
    #goJuice = "/v2/assets/fields/?assets=" + str(etID) + "&fields=7&limit=10"

    conn.request(
        "GET", "/v2/assets/fields/?assets=" + str(etID) + "&fields=6&limit=10", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)

    for i in json_output:
        #print(i['field'])
        #print(i['value'])
        riskOut = (i['value'])


    #print(riskOut)
    return riskOut

def find_severity(etID):
    #print(etID)
    sevOut = 0
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'assetID': ''
    }
    #goJuice = "/v2/assets/fields/?assets=" + str(etID) + "&fields=7&limit=10"

    conn.request(
        "GET", "/v2/assets/fields/?assets=" + str(etID) + "&fields=7&limit=10", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)

    for i in json_output:
        #print(i['field'])
        #print(i['value'])
        sevOut = (i['value'])


    #print(sevOut)
    return sevOut

def calc_pdc(dueUni):
    pdc = 5
    nowStamp = int(time.time()) 
    #gap = -1 * (dueUni - nowStamp) / 86400 
    gap =(nowStamp - dueUni) / 86400
    
    if gap > 56:
        pdc = 0
    elif gap > 49:
        pdc = 1
    elif gap > 35:
        pdc = 2
    elif gap > 28:
        pdc = 3
    elif gap > 14:
        pdc = 4
    else:
        pdc = 5

    """ print(gap)
    print(pdc) """


    return pdc

def buildArrayofTasks(limited):
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization' : 'Basic %s' %  userAndPass,
        'assetID': ''
    }
    conn.request("GET", "/v2/tasks/?limit=" + str(limited) + "&status=0", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)


    FCA = [] #"taskID","assetID","severity","risk","pdc","FC"
    keyGuide = "taskID,assetID,severity,risk,pdc,FilterCode"

    """ with open('APIpy.json') as f:
        data = json.loads(f.read())
        #print(data[0]['taskID'])
    """
    for i in json_output:
        #print(i['taskID'])
            #with taskID
        #print(i['assetID'])
            #with assetID
        #print(" - ")
        #FCA += [i] # & "-"

        thisRisk = find_risk(i['assetID'])
        thisSev = find_severity(i['assetID'])
        thisPDC = calc_pdc(i['due'])
        thisFC = calc_filterCode(thisRisk, thisSev, thisPDC)

        FCA += [i['taskID']]
        FCA += [i['assetID']]
        FCA += [thisSev]
        FCA += [thisRisk]
        FCA += [thisPDC]
        FCA += [thisFC]
        #FCA += [("-")]
    #f.close()
    print(keyGuide)
    print(FCA)


buildArrayofTasks(522)


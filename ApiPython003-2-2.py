import time
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode
from json import dumps, loads
from pprint import pprint

def calc_filterCode(risk, sev, pdc):

    return bigFC

def calc_pdc(dueUni):
    pdc = 5
    nowStamp = int(time.time()) 
    gap = -1 * (dueUni - nowStamp) / 86400 
    
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

    """     print(gap)
    print(pdc) """


    return pdc

#calc_pdc(1643944814)

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
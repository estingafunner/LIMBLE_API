#pip install pillow
#pip install openpyxl

""" 
RiskyBusiness will scour the relevant downtime excel sheet on the s/Drive, and create an array of 
RISK ratings and a matching array of equipment numbers. Those arrays will be sent to LIMBLE via API (seperate function/file)
 """

# - THIS IS WHAT IS NEXT - ##############
""" 
6.18 -  P067 - Adamatic / SL
        P068 - Stringline
        P069 - MainLine
        P070 - 
        P071 - BreadLine
        P072 - MuffinLine
        Organize info from downtime.xlsx, col D, into 4 categories (above), then apply RISK to those downtime minutes, then update assets with new RISK info via API



 """
#########################################
from openpyxl import load_workbook
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode

def getAssets():
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
    }
    conn.request("GET", "/v2/assets", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)
    #print(json_output)

    for i in json_output:
        #print(i['name'])
        riskOut = (i['name'])
    #END FOR-i

    with open('assets.json', 'w') as f:
        json.dump(json_output, f)

    return riskOut
#END getAssets()

getAssets()
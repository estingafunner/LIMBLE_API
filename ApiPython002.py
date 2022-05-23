
#import requests
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode
from json import dumps, loads
from pprint import pprint



conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
payload = ""
userAndPass = b64encode(b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

headers = {
    'Authorization' : 'Basic %s' %  userAndPass,
    'assetID': ''
}
conn.request("GET", "/v2/tasks/?limit=4&status=0", payload, headers)

res = conn.getresponse()
data = res.read()

json_output = json.loads(data)


FCA = [] #taskID, assetID, due


""" with open('APIpy.json') as f:
    data = json.loads(f.read())
    #print(data[0]['taskID'])
 """
for i in json_output:
    print(i['taskID'])
    print(i['assetID'])
    print(" - ")

    FCA += [i['taskID']]
    FCA += [i['assetID']]
#f.close()

print(FCA)

#Prints in json format
#pprint(json_output)

#data.decode("utf-8")
with open("APIpy.json", "w") as write_file:
    json.dump((json_output), write_file)

#json_str = json.dumps(json_output)
#print(json_str)

#print(data.decode("utf-8"))  ###-THIS IS RAW OUTPUT

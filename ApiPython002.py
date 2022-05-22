
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
conn.request("GET", "/v2/tasks/?name=UPDATED%20TASK&limit=5&status=0", payload, headers)

res = conn.getresponse()
data = res.read()

json_output = json.loads(data)

pprint(json_output)
#print(data.decode("utf-8"))  ###-THIS IS RAW OUTPUT

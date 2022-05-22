#Write your code here :-)
import http.client
from http.client import HTTPSConnection
from base64 import b64encode

conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
payload = ""
userAndPass = b64encode(b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

headers = {
    'Authorization' : 'Basic %s' %  userAndPass,
    'assetID': ''
}
conn.request("GET", "/v2/assets/?limit=10&orderBy=-lastEdited", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# require 'json'
# my_object = { :array => [1, 2, 3, { :sample => "hash"} ], :foo => "bar" }
# puts JSON.pretty_generate(data.decode("utf-8"))

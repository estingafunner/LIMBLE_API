import json
#WORKS with ApiPython002.py which runs the API and creates/updates the APIpy.json
#PREVIOUS AapiPython002-3.py can loop through the .json and pull specfic data points
#THIS will build array with 'for i' loop FCA = [(taskID), (due {run PDC function}), (assetID), (risk), (severity), (PDC)

FCA = [] #taskID, assetID, due


with open('APIpy.json') as f:
    data = json.loads(f.read())
    #print(data[0]['taskID'])

for i in data:
    print(i['taskID'])
    print(i['assetID'])
    print(" - ")

    FCA += [i['taskID']]
    FCA += [i['assetID']]
f.close()

print(FCA)

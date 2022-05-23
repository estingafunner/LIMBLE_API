import json
""" 
f = open('APIpy.json', )

data = json.loads(f)
 """

with open('APIpy.json') as f:
    data = json.loads(f.read())
    print(data[0]['taskID'])

for i in data:
    print(i['taskID'])

f.close()

""" for key in data:

    print(key, ":", data[key]) """
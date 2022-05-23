import json

f = open('APIpy.json', 'r')

data = json.load(f)


#for i in data:


print(data[1]['taskID'])

f.close()

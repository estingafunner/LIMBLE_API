import json

f = open('APIpy.json', 'r')

data = json.load(f)


#for literallyAnything in data:

print(data[1]['taskID'])

f.close()

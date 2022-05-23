import json

f = open('APIpy.json', )

data = json.loads(f)


""" for i in data[1]:
    print(i)

f.close() """

for key in data:

    print(key, ":", data[key])
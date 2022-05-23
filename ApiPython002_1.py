import json

with open('APIpy.json') as data_file:    
    data = json.loads(data_file.read())

#print(data)

for v in data:
    print("hey...")

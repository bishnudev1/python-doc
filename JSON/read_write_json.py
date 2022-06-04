
import json

file = open('posts.json','r')
x = file.read()

finaldata = json.loads(x)

for a in finaldata:
    print(a['title'],a['userID'])
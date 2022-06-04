import json

x = '{"course": "JSON", "fees": 2000, "duration": "1 Month"}'

y = json.loads(x)

print(y)

for items in y:
    print(items)
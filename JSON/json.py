import json

d = {
    'course':'JSON',
    'fees':2000,
    'duration':'1 Month'
}

f = json.dumps(d)

print(f)

import json

# Creating a dictionary
Dictionary ={1:'Welcome', 2:'to',
			3:'Geeks', 4:'for',
			5:'Geeks'}

# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary)
print('Equivalent json string of input dictionary:',
	json_string)
print("	 ")

# Checking type of object
# returned by json.dumps
print(type(json_string))

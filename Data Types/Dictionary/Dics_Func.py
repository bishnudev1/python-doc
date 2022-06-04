
# Iteration Functions in Dictionary


d = {
    'course':'Python',
    'duration':'3 Months',
    'source':'Github'
}

# get() Function -> Returns the value according the keys

print(d.get('duration'))

# keys() Function -> Get the keys of a dictionary

print(d.keys())

# Values() Function -> Get the values of a dictionary

print(d.values())

# items() Function -> Get all the items (Keys + Values)

print(d.items())

# Deletion Functions in Dictionary

# pop() method

d.pop('source')

print(d)

# del() method

del d ['duration']
# del(d)

print(d)

# dict method -> Creating a Dictionary

D = dict(name='Bishnudev',hobby='Coding')

# Update method

d.update({
    'course':'Django'
})

print(d)

# Clear method -> Clear whole Dictionary

d.clear()

print(d)

# Insert method

d['desc'] = 'This is a Python tutorial'

print(d)
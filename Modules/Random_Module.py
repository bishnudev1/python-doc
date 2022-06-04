

# Random Modules and it's functions

import random

# Randint -> Generates a random between two range

print(random.randint(1,9))

# Randrange -> Generates two random between except last range number

print(random.randrange(2,4))

# Random Choice -> Generate a random number in a list

l = [1,2,3,4,5,6]

print(random.choice(l))

# Random -> Generate a float number 

print(random.random())

# Shuffle -> Shuffle the list 

random.shuffle(l)
print(l)

# Uniform -> Generates a random float value between range

print(random.uniform(1,5))

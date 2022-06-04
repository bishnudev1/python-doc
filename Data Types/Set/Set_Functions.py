
# Iteration in Sets

s = {10,20,30,'Sets','Unorder','Unindex'}

for items in s:
    print(items)

S = {20,10,30,50,90}

# Set Function -> Convert a List into a Set

l = ['Hello','Hi','Greetings','Hola','Hay']
print(set(l))

# add() Function

S.add(80)
print(S)

# pop() Function

S.pop()
print(S)

# Remove Function

S.remove(30)
print(S)

# Clear Function

S.clear()
print(S)

# Discard Function

S.discard(20)
print(S)

# Update Function -> Creates a new Sets from a old Set

new_s = [10,20,30,120]

S.update(new_s)
print(S)

t = (10,20,30,'Tuple','Immutable')

l = len(t)

for a in range(l):
    print(t[a])

for items in t:
    print(items)

T = (10,20,30,40,50,10,10)

# Min-Max in Tuple

print(min(T))

print(max(T))

# Count in Tuple

print(T.count(10))

# Index in Tuple

print(T.index(40))

# Sum in Tuple -> Sum all the only integers items 

print(sum(T))
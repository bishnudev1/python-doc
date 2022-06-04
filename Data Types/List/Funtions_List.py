l = [2,8.4,"Bishnudev",False]

#  How to delete any item in a List ?

# Del Function

del(l[2])
print(l)
# Pop Function
l.pop(2)
print(l)
# Remove Function
l.remove(2)
print(l)
# Clear Function
l.clear()
print(l)


l = [2,8.4,"Bishnudev",False,2]

# How to update any item in a list

l[0] = 9

print(l)

# Insert Function

l.insert(3,"UI Goku")
print(l)

# Append Function

l.append("UE Vegeta")
print(l)

# Extends Function

n = {2,3,4}
l.extend(n)
print(l)

# Count Functions -> Returns the occurance of a item in a List

print(l.count(2))

# Max Functions -> Returns the max number of a List

L = [9,4,5,1,2]

print(max(L))

# Min Functions -> Returns the max number of a List

print(min(L))

# Sort Functions -> Sort the list

L.sort()
print(L)

# Reverse Function -> Reverse the List

L.reverse()

print(L)

# Index Functions -> Return the index of a item in a List

print(L.index(1))

# Zip Function -> Used to iterate two List at the same time

l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]

for a,b in zip(l1,l2):
    print(a,b)

# How to conver String into List ?

# 1st Method

str = input("Enter the value : ")

l = str.split()

print(l)

# 2nd Method

m = [str]

print(m)

# 3rd Method

L = []

for a in range(1,4):
    k = input(f"Enter the value of {a} : ")
    L.append(k)

print(L)
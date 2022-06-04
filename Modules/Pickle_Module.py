
import pickle

#  Pickle modules helps us to create and load python data in it
#  We can store List, Tuple or any object to a txt or other file 

l = [10,20,30,40,50,60,70,80,90,100]

file = open('writeData.txt','wb')

pickle.dump(l,file)

file.close()

#  Load in Pickle

# We can read our write file(decompressing) via load pickle


file = open('writeData.txt','rb')

l = pickle.load(file)
print(l)
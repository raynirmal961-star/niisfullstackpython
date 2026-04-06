import pickle
number=[10,20,30,40,50]
f=open("xyz.dat","wb")    #wb = write binary
pickle.dump(number,f)         #store list in binary file
f.close()
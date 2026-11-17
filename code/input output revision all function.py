# f = open("revision.txt","r")
# data = f.read()
# print(data)
# f.clse()

# f = open("revision.txt","r")
# line1 =f.readline()# line by line read krne ke liye code 
#data = f.read()# ek baar line ko read kr lia to dobara empty space print ho jayega
# print(data)
# print(line1)
# line2 =f.readline()
# print(line2)
# line3 =f.readline()
# print(line3)
# f.close()


# f= open("revision.txt","w") # ye mode file bhi create kr deta he 
# f.write("i am using writing mode and this mode overwrite all the data from the file")
# f.close()

# f= open("revision.txt","a")
# f.write("this mode use to add data at the end")
# f.close()


# f= open("revision.txt","r+")
# f.write("this mode use to overwrite the data at start")#no truncate,read and write,pointer start
# data =f.read()
# print(data)
# f.close()

# f= open("revision.txt","w+")
# #f.write("this mode use to overwrite the data at start")# complete data will be  truncate,read and write
# print(f.read())

# f.close()


# f= open("revision.txt","a+")
# f.write("this mode use to add the data at the end")# no truncate ,
# print(f.read())


# with open("revision.txt","r") as f:
#     print(f.read())


# with open ("revision.txt","w")as f:
#     f.write("ohh so you are come again")



#code for deleting a file(pip intall  __module install krne ke liye h)
import os
os.remove("practice.txt")
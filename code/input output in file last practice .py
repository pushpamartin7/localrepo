# with open("pushpa.txt","w") as f:
#     name =[]
#     for i in range(5):
#         val = input("name: ")
#         name.append(val+"\n")
#     f.writelines(name)   
    
# import os
# os.remove("pushpa.txt")

# with open("practice.txt","r")as f:
#     # f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")
#     data = f.read() 
#     new_data = data.replace("Java","Python")
#     print(new_data)

def check_word():
    word = "learning"

    with open("practice.txt")as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

# check_word()
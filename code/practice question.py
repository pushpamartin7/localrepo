#with open("practice.txt","a+")as f:
   # f.write("Hi everyone\nwe are learning file I/O\nusing Java.\nI like programming in Java")
# with open("practie.txt","r")as f:
#     data= f.read()
#     new_data= data.replace("Java","Python")
#     print(new_data)

#     with open("practie.txt","w")as f:
#       f.write(new_data)
def check_word():
    word = "learning"
    with open("practice.txt","r")as f:
        data = f.read()
        if((data.find(word)) != -1):
            print("found")
        else:
            print("not found")


    
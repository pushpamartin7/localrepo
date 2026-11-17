# import os
# os.remove("sample.txt")




def check_line():
    word = "learning"
    with open("practice.txt","r")as f:
        data = f.read()
        if( (data.check(word)) != -1):
            print("found")
        else:
            ("not found")
check_line()
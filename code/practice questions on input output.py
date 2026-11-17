# with open("revision.txt","w")as f:
#     f.write("Hi everyone \nwe are learning File I/O \nusing Java.\nI like programming in Java.")

# with open("revision.txt","r")as f:
#      data = f.read()
# new_data=data.replace("Java","python")    #output mei print kr dega lekin overwrite nhi karega 
# print(new_data)


# with open("revision.txt","w")as f:
#     f.write(new_data) # ab data overwrite hoga


 
# n = input("enter ypur word: ")
# def check_for_word(n):
#     with open("revision.txt","r")as f:
#         data = f.read()
    
#         if(data.find(n)) != -1:
#             print("found")
#         else:
#             print("not found")     
# check_for_word(n)



n = input("enter ypur word: ")

line_no = 1
def check_for_line(n):
    global line_no
    with open("revision.txt","r")as f:
        while True:
            data = f.readline()
            if not data:
                break

            if(n in data):
                print("found")
                print(f"at line number:{line_no}")
                return line_no
            line_no += 1 
    print("word not found")       
    return -1        
check_for_line(n)



#with open("revision.txt","r")as f:
    #data = f.read()
   # print(data)
    # num = "" 
    # for i in range (len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    #second method to print num




with open("revision.txt","r")as f:
    data = f.read()
    print(data)
    #num = "" 
    #nums = data.split(",")
    #print(nums)
    print(data.split(","))

count = 0   
with open("revision.txt","r")as f:
    data = f.read()
    num = data.split(",")
    for val in num:
        if (int(val) %2 == 0):
            count+=1
print(count)

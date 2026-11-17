# n = int(input("Enter the value of n: "))
# i = 1
# while i <= 10:
#     multi = n*i
#     print(multi)
    
#     i+=1
# print("Loop ended")
n = int(input("Enter the value of n: "))
list = [1,4,9,16,25,36,49,64,81,100,36]
i = 0
while i < len(list):
    if (list[i] == n):
        print("found at index",i)
        break
    else:
        print("finding...")
    i +=1
# list = [2,5,4,6,7]
# for el in list:
#     print(el)
# print(type(list))

# fruit = ("blackbeery","grapes","banana","apple")
# for val in fruit:
#     print(val)
# else:

#     print("All fruits are printed here")    




# # if else in for loop
# n ="Pushpa"
# for char in n:
#     if char == 'h':
#         print("h found")
#         break
#     print(char)
    
list = [1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)


tup = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = 0
for val in tup:
    if val == x:
        print("Found value at index", idx)
        break
    idx+=1



# i = 1
# while i <= 5:
#     print(i)
#     if( i == 3):
#         break
#     i += 1
# print("End of loop")


i = 0
while i <= 5:
    
    if( i == 3):
        i += 1
        continue

    print(i)
    i += 1
print("End of loop")

x = 0
while x <= 20:
    if x %2 != 0:
        x+=1
        continue
    print(x)
    x +=1
print("All even values printed") 
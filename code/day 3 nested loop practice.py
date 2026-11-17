# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=' ')
#         j+=1
#     print()
#     i += 1

# for n in range(6,0,-1):
#     for j in range(6,n-1,-1):
#         print(j,end=' ')
#         j-=1
#     print()
#     n-=1
    
# food =input("food: ")
# eat ='yes' if food == "jalebi" or food == "samosa"  else "no"
# print(eat)
age = int(input("age: "))
vote = ('yes', 'no')  [age < 18]
print(vote)
# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print("hello")
#     i +=1

# num =[1,2,3,4,5,4,3,2,1]
# num1 =num.reverse()
# print(num1)
# if num1 == num:
#     print("palidrome")
# else:
#     ("not a palindrome")
 
# n = int(input("enter n: "))

# sum =0 
# while n > 0:
#     sum = sum + (n% 10)**2
#     n  = n// 10
# print(sum) 

# n = "pushpa martin"
# for char in n:
#     if char == "p":
#         print("found")
#         break
#     print(char)

n = int(input('enter a value: '))
# for i in range (1,11):
#     print(n*i)

fact = 1
for i in range (1,n):
    fact = fact * i
    
print(fact)

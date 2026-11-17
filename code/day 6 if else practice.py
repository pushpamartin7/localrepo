# # num = int(input("Enter a no.: "))
# # if num % 2 == 0:
# #     print("value is even",num)
# # else:
# #     print("value is odd")
# # print("code is end")

# # num1 = int(input("num: "))
# # if num1 % 7 == 0:
# #     print("multiple of 7")
# # else:
# #     print("not multiple")


# a = int(input("Enter a no.: "))
# b = int(input("Enter a no.: "))
# c = int(input("Enter a no.: "))
# d = int(input("Enter a no.: "))
# if a>b and a>c and a>d:
#     print("a is greater")
# elif b>a and b>c and b>d:
#     print("b is greater")
# elif c>a and c>b and c>d:
#     print("c is greater")
# else:
#     print("d is greater")

marks = [43, 56.6, 54, 87.6, 23, 65.4, 87.0, "Pushpa", "martin", "nidhi"] #string is immutable and list is mutable
print(type(marks))# but we can chage value string into string but not into int
print(marks[6:10])
marks[9] = "Jyoti"  # allowed in python
print(marks)
print(len(marks))

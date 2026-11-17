#factorial

# n = int(input("enter value: "))
# def fact(n):
#      if (n==0 or n==1):
#           return 1
    
#      return fact(n-1) * n
# print(fact(n))


# desending number
# n1 = int(input("enter value: "))
# def sum(n1):
#      if (n1==0 or n1==1):
#           return 1
#      print(n1)
#      return sum(n1-1)


# print(sum(n))
#n1 = int(input("enter value: "))
# def fact(n1):
#      if(n1 == 0 or n1 == 1):
#           return 1
#      else:
#           return fact(n1-1) * n1

# print(fact(n1))

# n = int(input("enter value: "))
# def sum(n):
#     if (n == 0):
#         return 0
    
#     return sum(n-1)+n
# print(sum(n))

list = ["america","india","britain","china","russia"]
i = 0
def print_list(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list,idx+1)

    

(print_list(list))

def reverse(n):
    
    if n == 0:
        return
    print(n)
    reverse(n-1)
    
n =int(input("enter the value: "))
reverse(n)
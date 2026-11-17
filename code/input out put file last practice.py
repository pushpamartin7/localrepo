# class student:
#     name = input("enter name: ")
#     age = 26
#     religion = "Christian"
# s1 = student()
# print(s1.name)
# print(s1.age)
# print(s1.religion)


class student:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new value.....to the database")
    

s1 =student("pushpa")
print(s1.name)
s2 = student("angel")
print(s2.name)
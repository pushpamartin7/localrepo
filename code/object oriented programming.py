#class student:
#   name = "Pushpa"

# s = student()
# print(s.name)

# class car:
#     color = "red"
#     brand = "martin's"

# c1 = car()
# print(c1.color)
# print(c1.brand)

class student:
# default constructor
    def __init__(self):
            print("adding new student in Database")

  # parametrized constructor  
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

        print("adding new student in Database")

s1 = student("karan",76)
print(s1.name,s1.marks)

s2 = student("nirmal",67)
print(s2.name,s2.marks)

s3 = student('Pushpa',99)
print(s3.name,s3.marks)
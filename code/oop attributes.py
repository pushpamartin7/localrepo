class student:
    college_name = "Pushpa"
    name = "anonymous"
    def __init__(self,name,marks):

        self.name = name
        self.marks = marks
    
        print("adding new student in Database")
    def welcome(self):
       print("welcome student",self.name)

s1 = student("karan",87)
print(s1.name,s1.marks)
s1.welcome()

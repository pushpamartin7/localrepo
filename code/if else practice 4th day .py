# code for traffic light
"""light = (input("light color: "))
if(light == "yellow"):
    print("look")
elif(light == "green"):
    print("be ready")

elif(light == "red"):
    print("stop")

else:
    print("light is broken")"""

# marksheet print out 
"""marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Grade A")
elif marks >=70 and marks < 80:
    print("Grade B")
elif marks >= 60 and marks < 70:
    print("Grade C")
else:
    print("Grade D")"""

A = 2 
G = "M"
A = 5 
G = "F"
A = int(input("A: "))
G = input("F/M: ")
if ((A == 1 or A == 2)and G == "M"):
    print("Fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("Fee is 200")
elif(A == 5 or G == "M"):
    print("Fee is 300")
else:
    print("No fee")

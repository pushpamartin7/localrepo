# f = open("demo.txt","w")
# f.write("now i am prepared completely to get a job")  
# f.close()

f= open("demo.txt","a+")
f.write("\ni am here again \nhow are you dude")
f.close()

# f =open("sample.txt","a")
# f.write("a mode mei file ka name dene se agar file axist bhi nhi krti to apne app create ho jata he")
# f.close()


# f =open("demo.txt","r+")
# f.write("this mode will truncate the file")#read kr sakte he or overwrite kr skte he data ko or pointer starting mei hata he

# f.close()


f =open("demo.txt","w+")
f.write("this mode will  do not truncate the file")#read kr sakte he or overwrite kr skte he data ko pr no truncate here
f.close()
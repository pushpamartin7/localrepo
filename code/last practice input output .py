with open ("pushpa.txt","r")as f:
    #f.write("i am gatting late please leave me\nfor a while \nbecause i need to have some food and them going foe a job")
    # line1 = f.readline()
    # print(line1)
    # line2 = f.readline()
    # print(line2)
    # f.close
    # n =f.readlines()
    # print(n)
    # v=f.read(30)
    # print(v)
    # f.close()

    # read lline by line code
    # str =" "
    # while str:
    #     str =f.readline()
    #     print(str)
    # f.close()

    #read all line except \n 
    str = " "
    size = 0
    tsize =0
    while str:
        str = f.readline()
        size = size + len(str)
        tsize = tsize+ len(str.strip())
    print(size)
    print(tsize)
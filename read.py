fileName = "landinfo.txt"

def spacing(string, desiredlength):
    len(string)
    for i in range(desiredlength-len(string)):
        string+=(" ")
    return string

def readLand():
    file = open(fileName,"r")
    lines = file.readlines()    # returns the values as list 
    # lines = file.read()  # It returns the txt file as it is 

    list = []
    for i in lines:
        list.append(i.strip().split(","))
    print() 
    print("   "*3,"==="*10+" Megha's Land Rental System "+"==="*10)
    print(" "+"--"*55)
    print("|  Kitta No  |        Location       |   Direction   |     Area     |    Monthly Rent   |     Availability     | ")
    print(" "+"--"*55)
    
    for l in range(len(list)):
        
        print("|  "+spacing(list[l][0],10),end="")   
        print("|  "+spacing(list[l][1],21),end="")
        print("|  "+spacing(list[l][2],13),end="")
        print("|  "+spacing(list[l][3],12),end="")
        print("|  "+spacing(list[l][4],17),end="")
        print("|  "+spacing(list[l][5],20),end="|")
        
        print() # it breaks from one line to another line of the above parameter.
    print(" "+"--"*55)

def getLandDict():
    land = {}
    list= []
    file = open(fileName,"r")
    lines = file.readlines()    # returns the values as list 
    # for i in lines:
    #     kitta, city, direction, area, price, status = i.strip().split(",")
    #     land[kitta] = city,direction,area, price,status
    # file.close()
    # return land   
    for i in lines:
        list.append(i.strip().split(","))

    list2 = []
    list3 = []
    for j in range(len(list) ) :
        string = list[j][0]
        for k in range(1,len(list[j])):
            list2.append(list[j][k])
        list3.append(list2)
        list2 = []
        #  Adding the list to the dictionary 
        for z in list3:
            land[string] = z   

    return land  

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [0, 2, 3, 4, 5, 6, 7, 8, 9]

# extra
def generateList () :
    listOne = makeList(0,10,20) 
    listTwo = makeList(0,10,20)
    lookforSimalarities(listOne,listTwo)
    
def makeList (min,max,length) :
    tempList = []
    for i in range(0,length,1) :
        tempList.append(random.randint(min,max))
    return tempList   

# assigment
def lookforSimalarities (listOne,ListTwo) : 
    same = []
    for i in listOne :
        for x in ListTwo :
            if i == x : 
                same.append(i)
    print(same)



            

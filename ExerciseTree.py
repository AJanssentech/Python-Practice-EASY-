listOne = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def main() : 
    for x in listOne : 
        if x <= 5 : 
            print(x)

def extraOne() : 
    extralist = []   
    for i in listOne : 
        if i <= 5 :
            extralist.append(i)
    print(extralist)

def extraTwo() :
    extralist =[]
    look = input("Please enter a number\nWe'll look if there any numer smaller in the list\n")
    print("The numbers that is smaller than your nummer")
    for j in listOne :
        if (int(look) > j) : 
            extralist.append(j)
    print(extralist)
                 
main()
extraOne()
extraTwo()

    

def main() : 
    listOne = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for x in listOne : 
        if x <= 5 : 
            #print(x)
            #Extra's 
            extraList = []
            extraList.append(x)
            print(extraList)
    look = input("Please enter a number\nWe'll look if there any numer smaller in the list\n")
    print("The numbers that is smaller than your nummer")
    for i in listOne : 
        if int(look) >= int(i) :
            print(i)      



main()        
import sys
number = 0

def main () : 
    print("Welkom,")
    name = input("What is your name ?\n")
    age = input("What is your age asswell?\n")
    print ("Your name is " + name)
    number = 100 - int(age)
    print("You'll be 100 in " + str(number) + " years.")
    ask = input("Do you want to continue? \n press 1 \nDo you want to stop ? \n press 2\n")
    # Extra's 
    if int(ask) == 1 : 
        print ("Going to continue")
        amount = input("Please enter a number well print the amount of times you'll be 100\n")
        i = 0
        while i < int(amount) : 
            print("You'll be 100 in " + str(number) + " years.")
            i += 1 
            if i == amount : 
                break 
           
    elif int(ask) == 2 : 
        print("System shutdown")
        exit()


 


main()    
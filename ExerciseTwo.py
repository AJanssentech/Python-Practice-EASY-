def main () : 
    print("Welkom\nThis program will tell you if a number is even or odd")
    number = input("Please choose a number\n")
    if int(number) %4 ==0 : 
        print("This is a multiple by 4")
    elif int(number) %2 == 0 : 
        print("The number is even")
    elif int(number) %2 != 0 : 
        print("The number is odd") 
    print("do you want to type in 2 number and see if the devide each other ")
    answer = input("Press 1 for YES\npress 2 for NO\n") 
    print(answer)
    if int(answer) == 1 : 
        print("well continue")
        extra()
    elif int(answer) == 2 :
        print("System shutdown")
        exit() 
def extra() : 
    num = input ("Please enter the number you want to use that you later want to see if it devides\n")
    check = input("Please enter the number you want to devide it by\n")

    if int(num) %int(check) == 0 :
        answer = int(num) / int(check)        
        print ("The answer is\n" + str(answer)) 
    else : 
        print("The outcome has too many decimals")                                  

main()        
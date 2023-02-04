Factorial = True
name = input("\nPlease enter your sweet name...")
while(Factorial == True):
    print("\nEnter '1' to factorialize the number and '2' to exit...")
    choice = int(input("\nEnter your choice: "))
    if(choice == 1):
        Factorial = True
        print("\nWe will convert your normal value to factorialized value here :)")
        num = int(input("\nEnter the number to get factorialized: "))
        value = 1
        if (num < 0):
            print(f"\nSorry Mr/Mrs.{name}, The nagative numbers can't be factorialized...")
        elif (num == 0):
            print(f"\nWelcome Mr/Mrs.{name}, The factorial of 0 is 1")
        else:
            for fact in range(1,num+1):
                value = value * fact
            print(f"\nWelcome Mr/Mrs.{name}, The factorial of {num} is {value}")
    elif(choice == 2):
        Factorial = False
        print(f"\nWelcome Mr/Mrs.{name}")
        print("\nBye Bye")
    else:
        print(f"\nEnter the proper choice, Mr/Mrs.{name}")
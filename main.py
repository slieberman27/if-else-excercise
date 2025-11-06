valueError = False

try:
    n = int(input("enter your number"))
    if n % 2 != 0:  #% is similar to division except it checks for a remainder meaning if the remainder of x/2 is not 0, it is even
        print("Werid")
    elif 2 <= n <= 5:
        print("Not Werid")
    elif 6 <= n <= 10:
        print("Werid")
    elif n >= 20:
        print("Not Werid")

except ValueError:
    print("error: enter a number")
    valueError == True
    while valueError == True:
        n = int(input("enter your number"))
        if n % 2 != 0:  #% is similar to division except it checks for a remainder meaning if the remainder of x/2 is not 0, it is even
            print("Werid")
        elif 2 <= n <= 5:
            print("Not Werid")
        elif 6 <= n <= 10:
            print("Werid")
        elif n >= 20:
            print("Not Werid")
        valueError = False

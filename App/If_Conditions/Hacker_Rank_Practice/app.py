""""""

# get number
n = input(" Enter number: ")
if(n > 0 and n < 101):
    remainder = n%2
    if(remainder > 0):
        print("Weird")
    else:
        if(n >= 2 and n <= 5):
            print("Not Weird")
        elif(n >= 6 and n <= 20 ):
            print("Weird")
        elif(n > 20):
            print("Not Weird")
else:
    print(n, " is not within 1 - 100")

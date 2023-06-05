import os
os.system("cls")

clientAge = int(input("Enter age: "))
if(clientAge >= 18):
    clientOccupation = str(input("Enter client occupation:(Student/Professional/Retiree): "))
    if (clientOccupation == "Student"):
         print("Get a Student account")
    elif (clientOccupation == "Professional"):
        print("Get a Professional account")
    elif (clientOccupation == "Retiree" ):
        print("Get a Retirement account")
    else:
        print( "There is no account available for this client")
else:
     print( "You are not old enough to get an account")
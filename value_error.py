#!/bin/user/python3
while True:
    try:
        number = int(input("Please enter a number : "))
        break
    
    except ValueError:    
        print("Not a number")
        
    except:
        print("An unknown error occured")

print("Thank you for entering a number")        

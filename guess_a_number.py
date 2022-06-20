#!/bin/usr/python3


#Guess a number between 1-10
#set a variable for the secret nummber

secret_number=9
while True:
        guess= int(input("Guess the Number : "))
        
        if guess == secret_number:
            print("Hey! You guessed right")
        
        elif guess != secret_number:
            print("you guessed wrong!")
        break    

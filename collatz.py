# collatz.py
# author - Niall Wynne
# Week 4 Task
# Program that that asks the user to input any positive integer
# and outputs the successive values of the following calculation.

# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.

# Have the program end if the current value is one.

posint = int(input ('Please enter a positive integer: '))

def collatz(posint):                          #Looked on StackOverflow for help here
                                              # Most suggestions used a function
    while posint !=1:
        if posint% 2 == 0:
            posint= posint//2
            print(posint)

        else:
           posint=  3 * posint + 1
           print(posint)

collatz (posint)

# Initially tried to solve just using some loops from lectures but could not figure out the continuation.
# Had the program carrying out the initial calculation.
# Looked at some solutions that had a continue element but this one was shorter and I found it easier to understand.
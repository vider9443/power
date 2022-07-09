#Serendipity Booksellers
from os import system, name

from setuptools import Command

def clear():        #this function is used to clear unwanted text from the commandline
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

while True:
    print("\n\tSERENDIPITY BOOKSELLERS")
    print('\nHello customer, Welcome to Serendipity Book Club \n')
    print("\nType 'points' to view the number of points you have\nType 'quit' to end the program")
    command = (input("\nEnter command:\n")).lower()
    if command == "quit":
        print("You have quit the program.")
        break
    if command == "points":    
        while True:
            clear()
            #book club
            numberOfBooks = int(input('Enter the number of books purchased this month:'))

            #points awarding
            if numberOfBooks <= 0:
                print('Points awarded is: 0')
                break
            elif numberOfBooks <= 1:
                print('Points awarded is: 6')
                break
            elif numberOfBooks <= 2:
                print('Points awarded is: 16')
                break
            elif numberOfBooks <= 3:
                print('Points awarded is: 32')
                break
            else:
                print('Points awarded is: 60')
                break
    else:
        print("Invalid input!")
        clear()
        continue        

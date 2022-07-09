#sales tax challenge
from os import system, name

from setuptools import Command

def clear():        #this function is used to clear unwanted text from the commandline
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

square_feet = 0
labor_hours = 0
charge_per_hour = 20.00
price_of_paint = 0
no_of_gallons = 0
while True:
    print("\n\n\tPAINT COMPANY")
    print("\nType 'calc' to calculate the costs\nType 'quit' to end the program")
    command = (input("\nEnter command:\n\t")).lower()
    if command == "quit":
        print("You have quit the program.")
        break

    if command == "calc":    
        while True:
            clear()
            print("\tPAINT COMPANY CALCULATOR")
            square_feet = float(input("\nEnter amount of wall space in squarefeet:\n\t"))
            price_of_paint = float(input("\nEnter the price of paint per gallon in USD$:\n\t"))
            no_of_gallons = (square_feet * 1 / 115)
            no_of_gallons = round(no_of_gallons, 2)
            labor_hours = (square_feet * 8 / 115)
            labor_hours = round(labor_hours, 2)
            cost_of_paint = (no_of_gallons * price_of_paint)
            cost_of_paint = round(cost_of_paint, 2)
            labor_charges = (labor_hours * charge_per_hour)
            labor_charges = round(labor_charges, 2)
            
            print("\nRequirements:\n1.Gallons:", no_of_gallons)
            print("2.Hours of labor:", labor_hours," hours")
            print("\nPaint cost: $", cost_of_paint)
            print("Labor cost: $", labor_charges)
            print("Total = $",labor_charges + cost_of_paint )
            break
    else:
        print("Invalid input!")
        clear()
        continue    
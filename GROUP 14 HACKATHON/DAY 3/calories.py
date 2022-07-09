# calories calculator
from os import system, name

def clear():        #this function is used to clear unwanted text from the commandline
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

while True:
    print("\n\tCalories Calculator\n")
    print("\nType 'calc' to use calculator\nType 'quit' to exit program")
    command = (input("\nEnter command:\n")).lower()
    if command == "quit":
        print("You have quit the program.")
        break
    if command == "calc":
        while True:
            clear()
            #Entering fat grams consumed in a day
            fat = float(input("\nEnter the amount of fat in grams consumed:"))
            fat_calories = ( fat * 9)
            print("Calories from fat:", fat_calories, " grams")
            #Entering carbohydrates grams
            carbohydrates = float(input("\nEnter the amount of carbohydrates in grams consumed:"))
            carbohydrates_calories = carbohydrates * 4
            print("Calories from carbohydrates:", carbohydrates_calories," grams")
            break
    else:
        print("Invalid input!")
        clear()
        continue

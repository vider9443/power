# door lock system
import datetime
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")



print("Please set your password:")
password = input()


    
def check_password(pwd):
        clear()
        if pwd == password :
            is_correct = True
            print("\nAccess granted.\n")
        else:
            is_correct = False
            print("\nAccess denied.\n")
            pwd = input("Enter password:")
            check_password(pwd)
            return is_correct
    
door_closed = True
door_opened = False    
while True:
    login_time = "0000-00-00 00:00:00.000000"
    logout_time = "0000-00-00 00:00:00.000000"
    clear()
    print("\n\tMENU")
    print("\nType 'door' to access the door\nType 'quit' to exit the program")
    command = (input("\nEnter command:\n")).lower()
    if command == "quit":
        break    
    if command == "door":
        pwd = input("\nEnter password:\n")
        check_password(pwd)
    
        while True:
            print("\n\tDoor:")
            print("\nType 'open' to open the door\nType 'close' to close the door\nType 'quit' to exit door menu")
            open = "open"
            close = "close"
            quit = "quit"
            typed_input = (input("\nEnter command:")).lower()
            if typed_input == quit:
                    clear()
                    print("\nYou have exited the door program\n")
                    break

            while True:
                if typed_input == open and door_opened == False:
                    clear()
                    login_time = datetime.datetime.today()
                    print("\nThe door is now open\n")
                    print("The door was last opened at:", login_time)
                    door_opened = True
                    door_closed = False
                    break
                elif typed_input == open and door_opened == True:
                    clear()
                    print("\nThe door is already open\n")
                    print("The door was last opened at:", login_time)
                    break

                elif  typed_input == close and door_closed == False :
                    clear()
                    logout_time = datetime.datetime.today()
                    print("\nThe door is now locked\n")
                    print("The door was last closed at:", logout_time)
                    door_opened = False
                    door_closed = True
                    break
                elif typed_input == close and door_closed == True:
                    clear()
                    print("\nThe door is already closed\n")
                    print("The door was last closed at:", logout_time)
                    break
                else:
                    clear()
                    print("\nInvalid input!\n") 
                    break
      

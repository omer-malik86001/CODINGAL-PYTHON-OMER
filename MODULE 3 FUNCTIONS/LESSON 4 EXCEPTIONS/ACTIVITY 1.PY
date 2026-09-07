try:
    number = int(input("enter a number- "))
    print(f"the user entered {number}")
except ValueError:
    print("please enter a valid number not letters/symbols please. ")


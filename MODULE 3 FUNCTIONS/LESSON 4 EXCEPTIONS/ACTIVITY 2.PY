while True:
    try:
        number = int(input("enter a number- "))
        print(f"the user entered {number}")
        break
    except ValueError:
        print("please enter a valid number not letters/symbols please. ")

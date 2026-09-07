try:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    result=num1/num2
    print(f"the division result of {num1}/{num2}={result}")
except ValueError:
    print("ERROR:PLEASE ENTER A VALID NUMBERl. ")
except ZeroDivisionError:
    print("ERROR:PLEASE DO NOT DIVIDE BY 0")

else:
    print("HURRAY!NO EXCEPTIONS!")
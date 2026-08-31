# Take decimal number input from the user
decimal = int(input("Enter a decimal number: "))

# Handle the case if the number is 0
if decimal == 0:
    binary = "0"
else:
    binary = ""
    # Loop to divide by 2 and collect remainders
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

# Print the final binary result
print(f"Binary code: {binary}")

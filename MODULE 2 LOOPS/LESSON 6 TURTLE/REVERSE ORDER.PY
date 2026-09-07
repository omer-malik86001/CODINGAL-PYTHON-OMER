# Take numeric input from the user
number = int(input("Enter a number: "))

# Handle the case if the user enters a negative number
num = abs(number)

# Handle the edge case where the number itself is 0
if num == 0:
    count = 1
else:
    count = 0
    # Loop until the number becomes 0
    while num > 0:
        # Remove the last digit by performing integer division by 10
        num = num // 10
        # Increase the digit count by 1
        count += 1

# Display the final total number of digits
print(f"The total number of digits in {number} is: {count}")

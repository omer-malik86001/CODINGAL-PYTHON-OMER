import math

# Define the function to calculate circumference
def calculate_circumference(radius):
    # Formula: 2 * pi * r
    circumference = 2 * math.pi * radius
    return circumference

# Take the radius input from the user
try:
    user_radius = float(input("Enter the radius of the circle: "))
    
    if user_radius < 0:
        print("Radius cannot be negative.")
    else:
        # Call the function and get the result
        result = calculate_circumference(user_radius)
        
        # Display the result rounded to 2 decimal places
        print(f"The circumference of the circle is: {result:.2f}")

except ValueError:
    print("Please enter a valid numeric value.")

def sum(a,b):
    """prints the sum of a and b"""
    print(a+b)

print(sum.__doc__)

#____________________________________

# hello is the default value for the greeting arguement
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}")

greet("omer")

#_____________________________________
def square_root(x):
    return x ** (1/2)


print(f"the square root of 815 = {square_root(815)}")

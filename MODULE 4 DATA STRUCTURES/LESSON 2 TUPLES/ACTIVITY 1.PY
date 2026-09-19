numbers=[100,20,30,40,50]
print(numbers[0])
numbers[0]=999
print(numbers)

# TUPLE

tuple1=(100,20,30,40,50)
print(tuple1[1])
#tuple1[1]=78
print( len(tuple1) )

tupple2=(6,7,8)
combined=tuple1+tupple2
print(combined)
# THIS SHOWS HOW MANY TIMEDS A NUMBER COMES IN A TUPPLE/LIST
print(combined.count(7))
for i in combined:
    print(i)
print("data type of numbers:",type (numbers))
print("data type of combined:",type (combined))
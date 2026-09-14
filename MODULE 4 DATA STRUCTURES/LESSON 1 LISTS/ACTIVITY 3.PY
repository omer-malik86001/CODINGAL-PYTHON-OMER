numbers=[1,22,83,44,5,6,7,8,9,10]
# SUM OF THE NUMBERS IN THE LIST
sum=0
for i in numbers:
    sum=sum+i
print("sum of the numbers =",sum)     
avg=sum/len(numbers)
print(avg)
print(numbers[-1])
numbers.sort()
print(numbers)
print("smallest number",numbers[0]) 
print("largest number",numbers[-1])
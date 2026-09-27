items=["pencil","ruler","eraser","protractor"]

# TASK:filter out all items which start with the letter "p" (create a new list)

plist=[]

for i in items:
    if i[0]=="p":
        plist.append(i)
print(plist)

#list comprehension
plist=[
    i                   # what you want to add to the list 
    for i in items      # loop
    if i[0]=="p"]       # condition for filtering 
    
print(plist)

stockcnt=[100,200,50,80]
for item ,stock in zip(items,stockcnt):
    print(f"{item} = {stock}")
    
    #zip is used to loop over 2 lists simultaneously

#-------------------------------------------------------------------------------------------------------------------

inventory={item:stock for item,stock in zip(items,stockcnt)}

print(inventory)
# this is a dictionary comprehension!

#-------------------------------------------------------------------------------------------------------------------

numbers=[1,2,3,4,5]

#task:to square everny number in the list and create a new list 

result=[n*n for n in numbers]
print(result)
#another way to complete this is shown below


#-------------------------------------------------------------------------------------------------------------------

def square(n):
    return n*n

result=map(square,numbers)
print(list(result))
# MAP()-aapply the square function to very number in the less
    

    

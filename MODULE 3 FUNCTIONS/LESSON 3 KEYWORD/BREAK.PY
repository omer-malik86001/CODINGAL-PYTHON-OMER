#BREAK-STOP THE LOOP
# for i in range(20):
#     if i == 7:
#         break
#     print(i)

word="bannana"

#  THE MOMMENT THE FOR LOOP SEES UPERCASE A
# THE LOOP SHOULD STOP
# OTHERWISE, PRINT "A NOT FOUND"

for c in word:
    # we dont need to print the character
    #print(c)
    if c == "A":
        print("this is an uppercase a")
        break

else:
# THIS ELSE BELONGS TO THE FOR LOOP - THIS ELSE BLOCK WILL ONLY RUN IF THE FOR LOOP NEVER BREAKS 
     
    print("A NOT FOUND") 


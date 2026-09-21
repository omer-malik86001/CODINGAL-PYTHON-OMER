list1=[1,2,3,4,5,1,2,1,6,7,1,8]
print(list1)
print(type(list1))

set1={1,2,3,4,5,1,2,1,6,7,1,8}
print(set1)
print(type(set1))

fruits={"apple","bannana","apple","watermelon","bannana","watermelon"}
print(fruits)

# this code will not works in sets howerwer it can work in list and tuples print(fruits[0])

fruits.add("kiwi")
fruits.add("orange")
print(fruits)

print(len(fruits))

basket={"apple","grapes","bannana"}

#find the common elements in both sets

common_fruits=fruits.intersection(basket)
print(common_fruits)

#combine both sets and remove the duplicates

all_fruits=fruits.union(basket)
print(all_fruits)



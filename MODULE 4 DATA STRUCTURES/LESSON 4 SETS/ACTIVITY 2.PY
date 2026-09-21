#ARRAY=this only allows us to store data of a single data type

import array as arr
array1=arr.array("i",[1,5,9,77,])
print(array1)

array2=arr.array("f",[6.5,3.2,8.9,1.6])
print(array2)
#array1.reverse()
print(array1)

print(array1.count(77))
array1.append(56)
array1.insert(0,2)
print(array1)
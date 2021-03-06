#Create an array from the elements on index 0 and 2:
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr) 

#Create a filter array that will return only values higher than 42:

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
#or
filter_arr = arr > 42

newarr = arr[filter_arr]

#or
filter_arr = arr > 42

print(filter_arr)
print(newarr) 

#try by yourself:Create a filter array that will return only even elements from the original array.


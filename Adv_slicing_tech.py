#Question2

## Adv Slicing Techiques

""" Objective: The aim of this assignment is to master the art of slicing in Python lists.

Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it. """


##task 1 Given the list of temperatures:

print("="*60)

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print("Temperature for a given month are", temperatures)

print("="*60)

week_2_slice = temperatures[7:14]
print("Temperature for the 2nd week of the month are: ", week_2_slice)

print("="*60)
print("="*60)

#task 2 Extract all the temperatures above 100 (reminder: when slicing to the end of a list you don't need a stop index).


locator_100= temperatures.index(int(100)) ### the position of 100 from the list
print("Location of the first 100 temp on the list is at index",int(locator_100))

print("="*60)

####after finding the position create a slice.
temp_100_slice= temperatures[23: ]
print("this list shows all temperatures above 100", temp_100_slice)

#task3 extract temperatures from the 5th to the 10th.

##locating the the 5th to the 10th date index/position
### 5th - 1 = 4 on the index
### 10th - 1 = 9 on the index (please note: because the the last index position is not included when stopping the slice, i woudld have to stop it at index 10 (ironically :) )

dates_slice = temperatures[4:10] 
print("Temperatures from the 5th to 10th range from: ",dates_slice, "degress")

print("="*60)
print("="*60)



import numpy as np
import math

# Creates an array of specified length with random integers from 0-9999
def create_array(arraySize):
	return np.random.randint(10000, size=int(arraySize)) 

# Binary search algorithm
def binary_search(a, target):
	# Number of comparisons while searching
	comparisons = 0
	min = 0
	max = len(a)
	while min < max: # Will stop once reached smaller number (from left)
		x = min + (max - min) / 2
		val = a[x]
		if target == val:
			comparisons += 1
			print "Number of Comparisons it took to find: ", comparisons
			return x
		elif target > val:
			comparisons += 1
			if min == x: # Will stop once reached higher number (from right)
				break
			min = x
		elif target < val:
			comparisons += 1
			max = x

size = int(raw_input("What size would you like your array to be?> "))
a = create_array(size)
a.sort()
print a

target = int(raw_input("Pick target> "))

indexFound = binary_search(a,target)

if indexFound != None:
	print "Element " + str(target) + " found at index: " + str(indexFound)
else:
	print "Element not found."






#!/usr/bin/python

import pdb
import string

# Prints the first 10 letters of the alphabet
alpha = string.ascii_lowercase
first_ten = list([char for char in alpha[0:10]])
print(first_ten)

# First ten minus the sixth element ('f')
minus_sixth = list([char for char in first_ten if not char == 'f'])
print(minus_sixth)


f        = lambda x:[x, x+x, x+x+x]
grid     = list([f(x) for x in minus_sixth])
repeater = []
print([repeater.append(i) for x in grid for i in x])
# Have no idea why this thing prints None in every spot in the array. Something to do with lists being immutable? 
# I stepped through this one and the whole list is formed correctly up until it exits the loop and then all of the data inside repeater is lost.

# Returns minus_sixth with repeating elements of multiplicity 1, 2, and 3 as their own nested lists.
repeater_grid = list([f(x) for x in minus_sixth])
print(repeater_grid)

repeater_grid_caps = list([(j, i.capitalize()) for j, x in enumerate(repeater_grid, 1) for i in x if (j) % 3 == 0])
print(repeater_grid_caps)
# Still trying to figure out this one. Need to find out how to access the iteration index when I'm using list comprehension. Stack Overflow suggested
# using enumerate but this turns the list into tuples.

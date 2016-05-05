#!/usr/bin/python

import string

def main():
	squares_list_comp()
	squares_map()
	products()
	fn = ["function.py", "dog.py", "cat.txt", "red.py", "blue.c"]
	filenames(fn)
	string = "Ham and eggs ham and eggs have no legs"
	dictionary(string)

def squares_list_comp():
	squares = list([x**2 for x in range(0,10)])
	print(squares)

def squares_map():
	f = lambda x:x**2
	print(list(map(f, range(0,10))))

def products():
	f = lambda x, y:x*y
	print(reduce(f, range(1,6)))

def filenames(names):
	just_py = [name for name in names if name.find(".py") != -1]
	print(just_py)

# Having the same problem with immutability that i think i had in the list_comprehensions files
def dictionary(string):
	split_up = string.split()
	dictionary = set()
	dictionary_full = [dictionary.add(x) for x in split_up]
	print(dictionary_full)

main()
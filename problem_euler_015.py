#!/usr/bin/env python3
# 13.04.2017

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

param = 20
pathes = {}

def get_pathes(x,y):
	if (x,y) in pathes:
		return pathes[(x,y)]
	if x == 1:
		return y+1
	if y == 1:
		return x+1
	pathes[(x,y)] = (get_pathes(x-1,y) + get_pathes(x,y-1))
	return pathes[(x,y)]
		
print(get_pathes(param,param))

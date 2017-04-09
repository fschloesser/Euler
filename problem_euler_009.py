#!/usr/bin/env python3
# 04.04.2017

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52. There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

param = 1000

for a in range(param):
	for b in range(a,param):
		c = 1000-a-b
		if(a**2 + b**2 == c**2):
			print(a*b*c)
			exit


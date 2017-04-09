#!/usr/bin/env python3
# before 2012
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
from problem_euler_003 import *

def kgv(liste):
	primes = []
	for item in liste:
		primes.append(primefactors(item))
	print(primes)
	joined = []
	for item in primes:
		for thing in joined:
			try:
				item.remove(thing)
			except ValueError as e:
				pass
		joined.extend(item)
	print(joined)
	erg = 1
	for num in joined:
		erg = erg*num
	return erg

liste = []
for i in range(1,21):
	liste.append(i)
print(kgv(liste))

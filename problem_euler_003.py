#!/usr/bin/env python3
# before 2012
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def find_next_primefactor(start, num):
	it = start
	while it <= num+1:
		if (1.0*num/it).is_integer():
			return [it, num/it]
		it += 1

def primefactors(number):
	factors = []
	t = [2,number//2]
	while t[1] != 1:
		t = find_next_primefactor(t[0],t[1])
		factors.append(t[0])
	return factors

print(primefactors(600851475143))

#!/usr/bin/env python3
# 13.04.2017

# What is the value of the first triangle number to have over five hundred divisors?

import math

param = 500

def get_factors(p):
	factors = []
	for f in range(1,math.ceil(math.sqrt(p) - 1)):
		if p%f==0:
			factors.append(f)
			factors.append(p//f)
	sqrt = math.ceil(math.sqrt(p))
	if p == sqrt*sqrt:
		factors.append(sqrt)
	return factors

def triangle(n):
	return (n * (n+1)) // 2

n = 1
while (len(get_factors(triangle(n))) < param):
	n = n+1

print(triangle(n))

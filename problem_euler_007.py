#!/usr/bin/env python3
# 04.04.2017

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

param = 10001 

primes = [2]
def is_prime(i, primes):
	for j in primes:
		if i%j == 0:
			return False
		if j*j > i:
		    return True
	return True

while len(primes) < param:
	i = primes[-1]+1
	while not is_prime(i,primes):
		i+=1
	primes.append(i)

print(primes[-1])



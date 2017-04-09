#!/usr/bin/env python3
# 04.04.2017

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

param = 2000000

primes = [2]
def is_prime(i, primes):
	for j in primes:
		if i%j == 0:
			return False
		if j*j > i:
			return True
	return True

for i in range(2,param):
	if is_prime(i,primes):
		primes.append(i)

print(sum(primes))

#!/usr/bin/env python3
# 13.04.2017

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

collatz = {1: 1}
param = 1000000

def get_collatz(n):
	if n in collatz: 
		return collatz[n]
	if n % 2 == 0: 
		i = n/2
	else:
		i = 3 * n + 1
	collatz[n] = get_collatz(i)+1
	return collatz[n]
	
for n in range(1,param):
	get_collatz(n)

print(max(collatz, key=collatz.get))

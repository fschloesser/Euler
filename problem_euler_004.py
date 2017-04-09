#!/usr/bin/env python3
# before 2012
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def ispalindrome(number):
	liste = []
	while number > 0:
		liste.append(number%10)
		number = number//10
	for i in range(len(liste)):
		if liste[i] != liste[len(liste)-1-i]:
			return False
	return True

max = 1
for a in range(999,99,-1):
	for b in range(999,a-1,-1):
		if max < a*b and ispalindrome(a*b):
			max = a*b

print(max)

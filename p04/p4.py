"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

pals = []

for x in range(998001):
	if str(x) == str(x)[::-1]:
		pals.append(x)
pals=pals[::-1]

for p in pals:
	for n1 in range(100,1000):
		for n2 in range(100,1000):
			if (n1*n2) == p:
				print(p)
				print(n1)
				print(n2)
				sys.exit()

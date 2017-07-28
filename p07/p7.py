"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


import time,math

s=time.time()

numPrimes = 1
x=3
while numPrimes < 10001:
	check = False
	for i in range(2,int(x ** 0.5) + 1):
		if x % i == 0:
			check = True
	if check == False:
		numPrimes+=1
		print(numPrimes)
		print(x)
	x+=2 

print(time.time() -s)		

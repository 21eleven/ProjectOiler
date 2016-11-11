
import time

s = time.time()

def checkPrime( n ):
	if n < 2: 
		return false
	if n == 2 :
		return True
	for x in range(3, int(n ** 0.5) + 1, 2):
		if n % x == 0:
			return False

	return True

primes = [2]

next_odd = 3

sumPrimes = 2
while next_odd < 2000000:
	if checkPrime(next_odd):
		sumPrimes += next_odd
	next_odd +=2

print primes
print sum(primes) 
print sumPrimes
print time.time() - s

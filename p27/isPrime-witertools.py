from itertools import count, islice

def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0 or n <= 1:
		return False
	for i in islice(count(3,2),int(n**0.5)+1):
#	for i in range(3, int(n**0.5)+1, 2):
		print i
		if n % i == 0:
			return False
	return True

print isPrime(1463)

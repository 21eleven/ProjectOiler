import math,time

s = time.time()

def isPrime(num):
	limit = math.ceil(math.sqrt(num))
	i = 2
	while(i <= limit):
		if(num % i == 0):
			return False
		i+=1
	return True

def nthPrimeNumber(num):
	i=1
	n=3
	while(i<num):
		if(isPrime(n)):
			i+=1
		n+=2
	nthPrime = n -2
	print nthPrime

nthPrimeNumber(10001)
print time.time() - s

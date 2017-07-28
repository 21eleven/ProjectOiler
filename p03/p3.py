"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


decomp = 600851475143

with open('/home/noah/primes-to-100k.txt') as f:
	primes = f.read().splitlines()

i = 0

factors = []

while decomp > 2:
	prime = int(primes[i])
	if decomp % prime == 0:
		factors.append(prime)
		decomp = decomp / prime
		print(prime)
		print(decomp)
	i+=1

print(factors)

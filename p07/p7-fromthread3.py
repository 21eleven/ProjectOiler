import time

s = time.time()

def is_prime(n):
	n = abs(int(n))

	if n < 2 :
		return False

	if n ==2 :
		return True

	if n % 2 == 0 :
		return False

	for x in range(3, int(n ** 0.5) + 1, 2) :
		if n % x == 0 :
			return False

	return True

primes = [2]

next_odd = 3

while len(primes) < 10001 :
	if is_prime(next_odd) :
		primes.append(next_odd)
	next_odd += 2

print(primes[-1])
print time.time() - s

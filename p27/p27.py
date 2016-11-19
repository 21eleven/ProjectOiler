
def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0 or n <= 1:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

count = 0
check = True

maxCount = 0
maxA = 0
maxB = 0

for a in range(-999,1000):
	for b in range(-1000,1001):
		count = 0
		check = True
		while check == True:
			x = (count*count)+(count*a)+b
			check = isPrime(x)
			count += 1
		if count > maxCount:
			maxCount = count
			maxA = a
			maxB = b

print maxCount, maxA, maxB, maxA*maxB

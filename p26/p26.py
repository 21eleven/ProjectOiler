#the length of the repeating portion of an integer's reciprocal is the smallest value x where: (10^x) -1 % (integer) is 0.


def findRep(n):
	for x in range(1,1000):
		if ((10**x)-1) % n == 0:
			return x
maxRep = 0
maxNum = 0
for x in range(1,1000):
	rep = findRep(x)
	if rep > maxRep:
		maxRep = rep
		maxNum = x

print maxNum, maxRep


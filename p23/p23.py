
def abundance (n):
	divs = 1
	for x in range(2,int(n**0.5)+1):
		if n % x == 0:
			divs += x
			if (n/x != n) and (n/x != x):
				divs += n/x
	return divs>n

def findAbundants(n):
	abundants = []
	for i in range(3,n):
		if abundance(i):
			abundants.append(i)
	return abundants
a = findAbundants(28124)
nums = [n for n in xrange(28124)]

Sum = 0

abSums = []

for x in a:
	for y in a:
		abSums.append(x + y)

for n in nums:
	if n not in abSums:
		Sum+=n

print Sum



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

for n in nums:
	check = False
	x = 1
	while (x < int(n/2)+1) and check == False:
		if x in a and n-x in a:
			check = True
		x += 1
	if check == False:
		Sum += n

print Sum	 

	

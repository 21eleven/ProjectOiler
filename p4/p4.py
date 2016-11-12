import sys

pals = []

for x in range(998001):
	if str(x) == str(x)[::-1]:
		pals.append(x)
pals=pals[::-1]

for p in pals:
	for n1 in xrange(100,1000):
		for n2 in xrange(100,1000):
			if (n1*n2) == p:
				print p
				print n1
				print n2
				sys.exit()

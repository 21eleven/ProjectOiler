
sumOsqr = 0
sqrOsum = 0

for i in xrange(101):
	print i
	sumOsqr += (i*i)
	sqrOsum += i

sqrOsum = sqrOsum * sqrOsum

print abs(sumOsqr - sqrOsum)


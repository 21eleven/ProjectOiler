tnum = 1
nthTnum = 1

divisors = 0

def getNumDivisors( n ):
	divisors = 0
	for i in range(1,n+1):
		if n % i == 0:
			divisors+= 1
	return divisors

while divisors < 501:
	print nthTnum
	print tnum
	
	divisors = getNumDivisors(tnum)
	print divisors

	nthTnum+= 1
	tnum += nthTnum
	

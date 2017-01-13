import itertools

combs	= []
coins	= [1,2,5,10,20,50,100]

current = []

def nextCoin(l):
	thisL = l
	print l
	s = sum(thisL)
	if s == 200:
		combs.append(sorted(thisL,key=int))
		return 
	if s > 200:
		return
	for c in coins:
		print "starting {}".format(c)
		nextL = thisL
		nextL.append(c)
		nextCoin(nextL)

for start in coins:
	print "starting {}".format(start)
	lis = []
	lis.append(start)
	nextCoin(lis)

print len(combs)
	



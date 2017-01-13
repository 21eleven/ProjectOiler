combs = []
#coins = [1,2,5,10,20,50,100]
coins = [1,2]

def addCoins(lis):
	if sum(lis) == 2:
		combs.append(lis)
		return
	if sum(lis) > 2:
		print "{} terminating!".format(sum(lis))
		return
	else:
		for coin in coins:
			addCoins(lis)
			return
	

for c in coins:
	print c
	l1 = []
	l1.append(c)
	addCoins(l1)

print combs

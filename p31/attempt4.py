
combs = []

def add_coin(coins, target, part=[]):
	s = sum(part)
	if s == target:
		print part, target
		combs.append(part)
	if s >= target:
		return
	for i in range(len(coins)):
		n = coins[i]
		add_coin(coins, target, part+[n])

add_coin([1,2,5],10)


print len(list(set(combs)))

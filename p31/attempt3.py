import itertools

items = [1,2,5,20,50,100,200]
combs = []

value=200

items = [i for i in items if i<=value]

print items

for i in range(1,value+1):
	print "Phase {}".format(i)
	for c in itertools.combinations_with_replacement(items, i):
		if sum(c) == value:
			combs.append(c)

print len(combs)

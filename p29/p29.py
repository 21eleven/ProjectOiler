l  	= []

for a in range(2,101):
	for b in range(2,101):
		p=a**b
		if p not in l:
			l.append(p)

print len(l)

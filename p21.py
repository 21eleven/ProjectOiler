amicables = []

for i in range(2,10000):
	divs = [1]
	for x in range(2,int(i**0.5)+1):
		if i % x == 0:
			divs.append(x)
			divs.append(i/x)
	s = sum(divs)
	divs = [1]
	for y in range(2, int(s**0.5)+1):
		if s % y == 0:
			divs.append(y)
			divs.append(s/y)
	if i == sum(divs) and s != i:
		if s not in amicables:
			amicables.append(s)
		if i not in amicables:
			amicables.append(i)

print sum(amicables)

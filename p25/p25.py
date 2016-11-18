index, n1, n2  = 3, 2, 1

while len(str(n1)) < 1000:
	index +=1
	fib = n1 + n2
	n2 = n1
	n1 = fib

print index

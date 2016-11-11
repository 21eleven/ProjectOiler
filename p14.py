longestchain = 1
longestchainVal = 0

for x in range(13,1000000):
	count = 1
	n = x
	while n != 1:
		print n
		if n % 2 == 0:
			n = n/2
		else:
			n = n*3 + 1
		count+=1
	if count > longestchain:
		longestchain = count
		longestchainVal =  x

print longestchain
print longestchainVal 

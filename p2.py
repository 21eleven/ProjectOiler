low = 1
high = 1
nextNum = 0
sumFibs = 0

while nextNum < 4000000:
	if nextNum % 2 == 0:
		sumFibs += nextNum
	nextNum = low + high
	low = high
	high = nextNum

print sumFibs

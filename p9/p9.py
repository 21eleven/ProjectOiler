import sys

for a in range(1,1000):
	for b in range(1, 1000):
		c=( a**2 + b**2) ** 0.5
		if a+b+c == 1000:
			print a*b*c
			sys.exit()

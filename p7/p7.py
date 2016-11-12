
import time,math

s=time.time()

numPrimes = 1
x=3
while numPrimes < 10001:
	check = False
	for i in range(2,int(x ** 0.5) + 1):
		if x % i == 0:
			check = True
	if check == False:
		numPrimes+=1
		print numPrimes
		print x
	x+=2 

print time.time() -s		

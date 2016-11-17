import math

seq, f , i = list(range(10)), [], 9

n = 999999

while i >= 0:
	f.append(n / math.factorial(i))
	n %= math.factorial(i)
	i -= 1

result = []

for i in f:
	result.append(seq[i])
	del seq[i]

print result

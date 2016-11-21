
nums = []
power = 5

limit = (power+1)*9**power	#9**6 is the largest value a digit can contribute toward the sum of all the digits

print limit

for x in range(2,limit):
	s = str(x)
	sumX = 0
	for i in s:
		sumX += int(i)**power
	if sumX == x:
		nums.append(x)

print nums
print sum(nums)

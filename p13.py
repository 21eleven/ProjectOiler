#nums = [int(line.rstrip('\n')) for line in open('numbers-p13.txt') ]
#print str(sum(nums))[0:10]
print str(sum([int(line.rstrip('\n')) for line in open('numbers-p13.txt')]))[0:10]


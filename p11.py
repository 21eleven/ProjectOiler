
#with open('grid-p11.txt') as f:
#	content = f.readlines()

content = [line.rstrip('\n').split(' ') for line in open('grid-p11.txt')]

def horizontalProduct( l ):
	maxP = 0
	for y in xrange(len(l)):
		for x in xrange(len(l[y])-3):
			prod = 1
			subList = l[y][x:x+4]
			for p in subList:
				prod *= int(p)
			if prod > maxP:
				maxP = prod
	return maxP

def verticalProduct( l ):
	maxP = 0
	for y in xrange(len(l)-3):
		for x in xrange(len(l[y])):
			prod = 1
			subList = []
			for i in xrange(4):
				subList.append(l[y+i][x])
			for p in subList:
				prod *= int(p)
			if prod > maxP:
				maxP = prod
	return maxP

def rightDiagProduct( l ):
	maxP = 0
	for y in xrange(len(l)-3):
		for x in xrange(len(l[y])-3):
			prod = 1
			subList = []
			for i in xrange(4):
				subList.append(l[y+i][x+i])
			for p in subList:
				prod *= int(p)
			if prod > maxP:
				maxP = prod
	return maxP

def leftDiagProduct( l ):
	maxP = 0
	for z in xrange(len(l)):
		l[z] = l[z][::-1]
	for y in xrange(len(l)-3):
		for x in xrange(len(l[y])-3):
			prod = 1
			subList = []
			for i in xrange(4):
				subList.append(l[y+i][x+i])
			for p in subList:
				prod *= int(p)
			if prod > maxP:
				maxP = prod	
	return maxP 

hp  =  horizontalProduct(content)
vp  = verticalProduct(content)
rdp = rightDiagProduct(content)
ldp = leftDiagProduct(content)

maxP = 0 

if hp  > maxP:
	maxP = hp
if vp  > maxP:
	maxP = vp
if rdp > maxP:
	maxP = rdp
if ldp > maxP:
	maxP = ldp

print maxP


rows = [r.rstrip('\n').split(' ') for r in open('triangle-p18.txt')]
#rows = rows[::-1]

sums = []

def descendTree(rows, index, pathSum):
	if len(rows) == 1:
		pathSum += int(rows[0][index])
		sums.append(pathSum)
		return 0
	else:
		print len(rows)
		pathSum += int(rows[0][index])
		rows = rows[1:]
		descendTree(rows, index, pathSum)
		descendTree(rows, index+1, pathSum)
		return 0
		
descendTree(rows, 0 , 0)

print len(sums)
print max(sums)



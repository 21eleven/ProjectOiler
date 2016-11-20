interval=0
rep = 0
turn = 0

diagonals = []


for x in range(1,(1001**2)+1):
	if x == 1:
		interval = 2
		diagonals.append(x)
	elif rep == interval and turn == 3:
		diagonals.append(x)
		rep = 0
		turn = 0
		interval += 2

	elif rep == interval:
		rep = 0
		turn += 1
		diagonals.append(x)
	rep+= 1


print sum(diagonals)

def alphabetical_check(s1, s2):
	if s1[0] == s2[0] and len(s1) != 1 and len(s2) != 1:
		return alphabetical_check(s1[1:], s2[1:])
	elif s1[0] == s2[0] and len(s1) == 1:
		return True
	elif s1[0] == s2[0] and len(s2) == 1:
		return False
	elif s1[0] > s2[0]:
		return False
	else:
		return True


names = [line for line in open('p022_names.txt')][0].replace('"','').split(",")

for n in xrange(len(names)):
	for m in range(n+1,len(names)):
		if alphabetical_check(names[n],names[m]) == False:
			switch = names[m]
			names[m] = names[n]
			names[n] = switch


sumScore = 0
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

for i in xrange(len(names)):
	letterSum = 0
	for l in names[i]:
		letterSum += alphabet[l]
	sumScore += ((i+1)*(letterSum))

print sumScore

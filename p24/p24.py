
seq = "0123456789"
#seq = "1234"

seq = list(seq)

iteration = 0
print iteration
print seq
iteration += 1


def findK(s):
	end = len(s)-1
	check = end -1
	if (len(s) == 2) and (s[check] >= s[end]):
		return "Final"
	elif s[check] < s[end]:
		return check
	else:
		s = s[:end]
		return findK(s)

def lexopermutate(s):
	k = findK(s)
	if k == "Final":
		return k
	for i in range(k+1,len(s)):
		if s[i] > s[k]:
			l = i
	swap = s[l]
	s[l] = s[k]
	s[k] = swap

	a = s[:k+1]
	b = s[k+1:]
	b = b[::-1]
	
	return a+b
while (seq != "Final") and (iteration < 1000000):
	print iteration
	iteration += 1
	seq = lexopermutate(seq)
	print seq

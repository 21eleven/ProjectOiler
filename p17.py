
def digitToWord( d ):
	if d == '0':
		return ' '
	if d == '1':
		return 'one'
	if d == '2':
		return 'two'
	if d == '3':
		return 'three'
	if d == '4':
		return 'four'
	if d == '5':
		return 'five'
	if d == '6':
		return 'six'
	if d == '7':
		return 'seven'
	if d == '8':
		return 'eight'
	if d == '9':
		return 'nine'


def numberToWord( n ):
	s = str(n)
	s = s[::-1]
	words = []

	if len(s) == 1:
		return digitToWord(s)
	if len(s) == 2:
		if s[1] == '1':
			s = s[::-1]
			if s == '10':
				return 'ten'
			if s == '11':
				return 'eleven'
			if s == '12':
				return 'twelve'
			if s == '13':
				return 'thirteen'
			if s == '14':
				return 'fourteen'
			if s == '15':
				return 'fifteen'
			if s == '16':
				return 'sixteen'
			if s == '17':
				return 'seventeen'
			if s == '18':
				return 'eighteen'
			if s == '19':
				return 'nineteen'
		if s[1] == '0':
			return ' '+digitToWord(s[0])
		if s[1] == '2':
			return 'twenty '+digitToWord(s[0])
		if s[1] == '3':
			return 'thirty '+digitToWord(s[0])
		if s[1] == '4':
			return 'forty '+digitToWord(s[0])
		if s[1] == '5':
			return 'fifty '+digitToWord(s[0])
		if s[1] == '6':
			return 'sixty '+digitToWord(s[0])
		if s[1] == '7':
			return 'seventy '+digitToWord(s[0])
		if s[1] == '8':
			return 'eighty '+digitToWord(s[0])
		if s[1] == '9':
			return 'ninety '+digitToWord(s[0])
	if len(s) == 3:
		s2 = s[:2]
		s2 = s2[::-1]
		if s2 == '00':
			return digitToWord(s[2]) +' hundred'
		else:
			return digitToWord(s[2]) +' hundred and '+numberToWord(s2)

letters = ''

for x in range(0,1000):
	letters += numberToWord(x)
letters += 'one thousand'
letters = letters.replace(' ','')

print len(letters)


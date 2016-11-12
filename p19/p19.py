year=[31,28,31,30,31,30,31,31,30,31,30,31]
leapyear=[31,29,31,30,31,30,31,31,30,31,30,31]

days = 0
sundays = 0

for y in range(1901,2001):
	if y % 4 == 0 and y!= 1900:
		for m in leapyear:
			days += m
			if days % 7 == 5:
				sundays+=1
	else:	
		for m in year:
			days += m
			if days % 7 == 5:
				sundays+=1
	
print sundays

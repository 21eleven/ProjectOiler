

def factorial(number, product):
	if number == 1:
		p = [int(i) for i in str(product)]
		print sum(p)
	else:
		p = product * number
		n = number - 1
		factorial(n, p)

factorial(100,1)


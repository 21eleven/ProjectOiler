"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sumOsqr = 0
sqrOsum = 0

for i in range(101):
	sumOsqr += (i*i)
	sqrOsum += i

sqrOsum = sqrOsum * sqrOsum

print(abs(sumOsqr - sqrOsum))


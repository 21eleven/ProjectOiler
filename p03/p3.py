"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


decomp = 600851475143

i = 1

while decomp > 1:
    i+=2
    if decomp % i == 0:
        decomp/= i

print(i)

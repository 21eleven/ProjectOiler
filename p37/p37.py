"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def get_truncates(n):
    truncates = []
    truncates.append(n)
    
    for i in range(1,len(str(n))):
        truncates.append(int(str(n)[i:]))
        truncates.append(int(str(n)[::-1][i:][::-1]))


    return truncates

def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    square_root = n**0.5
    isqr = int(square_root) +1

    for i in range(3,isqr,2):
        if n % i == 0:
            return False

    return True
    

def check_truncates(lis):
    for n in lis:
        if is_prime(n) == False:
            return False
    return True

truncatable_primes = []
num = 9

#print(check_truncates(get_truncates(3797)))


while len(truncatable_primes) < 11:
    num += 2
    parts = get_truncates(num)
    if check_truncates(parts) == True:
        truncatable_primes.append(num)
        print(num)

print(truncatable_primes)
print(sum(truncatable_primes))


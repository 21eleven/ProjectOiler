import sys

def primeFinder(n):
    ## Returns all primes from 0 to n
    # here, all integers are prime until proven otherwise

    sieve = [True] * n # label 0 to n as True (Prime)

    # odd numbers from 3 to int(n**0.5)+1 which happen to be prime are useful
    # for making our prime sieve. 
    # Primes above int(n**0.5)+1 are not useful because when squared they are
    # greater than n. 

    for i in range(3, int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)

    # the odd numbers that are less than the first odd prime squared (5 and 7)
    # happen to be prime. So we dont have to worry about 
    #   if sieve[i]:
    # being evaluated as true when i is not prime for the values of i
    # that never had a chance to be filtered out because they are
    # less than nine.
    # All non-prime integers above 9 and up to n are filtered 
    # out by this line:
    #       sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    # or put more simply:
    #       sieve[i*i::2*i]=[False]*len(sieve[i*i::2*i))
    # so for i = 3 the above line is saying for all odd numbers from nine to n
    # that have 3 as a factor
    # (as represented by the expression sieve[i*i::2*i]) // see note below
    # label them as not prime, do this by broadcasting a list of
    # false values that is len(sieve::2*i) upon them 
    
    # Finally, return 2, the only even prime, and all the odd numbers that
    # we failed to prove where non-prime using our sieve

    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def makeParts(x):
    x = str(x)
    parts = [x]
    for i in range(1,len(x)):
        l, r = i, 0-i
        l, r = x[l:], x[:r]
        parts += [l] + [r]
    return parts

print(makeParts(3797))

truncatable_primes = []

search_space = 1000000

primes = primeFinder(search_space)

for i in range(9, search_space, 2):
    parts = makeParts(i)
    prime_parts = []
    for p in parts:
        if int(p) in primes:
            prime_parts += [p]
        else:
            break
    if set(prime_parts) == set(parts):
        truncatable_primes += [i]
        print(truncatable_primes)
    if len(truncatable_primes) == 11:
        print(sum(truncatable_primes))
        sys.exit()
"""
    for p in parts:
        if p in primes:
            prime_parts.append(p)
    if len(prime_parts) == len(parts):
        print("FOUND ", i)
        break"""

"""while(len(truncatable_primes) < 11):
    for i in range(9, search_space, 2):
        print(i)
        truncates = makeParts(i)
        check = True
        for n in truncates:
            if n not in primes:
                check = False
                break
            else:
                print(i, n)
        if check == True:
            truncatable_primes += [i]
            print("FOUND ",i)
        if check == True and len(truncatable_primes) == 11:
            break
    if len(truncatable_primes) == 11:
        break
    else:
        search_space *= 2
        print("... limit reached, remaking search space ", search_space)
        primes = primeFinder(search_space)


print(truncatable_primes)"""

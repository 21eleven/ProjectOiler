
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

print(primeFinder(200))


def slidingSieve(known_primes, sieve, filter_points, previous_checkpoint, next_checkpoint):
    # For when you want to continue building your sieve from where you 
    # last left off


    ## DOES IT EVEN MAKE SENSE TO ATTEMPT THIS????
    new_sieve = [True] * (next_checkpoint - previous_checkpoint)
    filter_pts = []

    if previous_checkpoint == 0:
        for i in range(3, int(n**0.5)+1,2):
            if sieve[i]:
                        
# [note] the python expression sieve[i*i::2*i] means: 
#   all odd numbers from i squared to n that have i as a factor
# why is it that the gap between these values of non-primes with a common factor
# i is i times two????
# Because when you have a sequence of a values that all have an odd integer i 
# as a factor they alternate between even and odd values

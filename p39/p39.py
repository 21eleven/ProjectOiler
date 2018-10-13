"""
leaned on Dickson's method from :
https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
"""

from collections import Counter

def find_factor_pairs(x):
    pairs = []
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            pairs.append((i,int(x/i)))
    return pairs

pythag_trips = set()

for i in range(4,200,2):
    r = i
    i = (i**2)/2
    for p in find_factor_pairs(i):
        s = p[0]
        t = p[1]
        x = r+s
        y = r+t
        z = r+s+t
        pythag_trips.add((x,y,z))

perimeters = Counter()
for triple in pythag_trips:
   perimeters[sum(triple)] += 1 
   
assert perimeters[120] == 3

print([perimeter for perimeter in perimeters.most_common() if perimeter[0] < 1000][0])


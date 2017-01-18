from fractions import Fraction

examples = []
Ns = []
Ds = []

def check(n1,d1):
    value1 = float(n1)/float(d1)
    if value1 >= 1:
        return False
    n2 = str(n1)[0]
    d2 = str(d1)[1]
    try:
        value2 = float(n2)/float(d2)
    except ZeroDivisionError:
        return False
    if value1 == value2 and(str(n1)[1] == str(d1)[0]):
        return True
    else: 
        return False


for a in range (10,100):
    for b in range (10,100):
        example = check(a,b)
        if example == True:
            Ns.append(a)
            Ds.append(b)
            examples.append("{}/{}".format(a,b))
print examples

N=1
D=1

for n in Ns:
    N *= n
for d in Ds:
    D *= d
print N,D,Fraction(N,D)


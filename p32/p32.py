pandigitals = []

def checkPandigital(s):
    if ('1' in s) and ('2' in s) and ('3' in s) and ('4' in s) and ('5' in s) and ('6' in s) and ('7' in s) and ('8' in s) and ('9' in s):
        return True
    else:
        return False

for x in range(1,101):
    for y in range(1,10000):
        product = x*y
        mmp = str(x)+str(y)+str(product)
        if len(mmp) > 9:
            break
        elif len(mmp) == 9:
            if checkPandigital(mmp) == True:
                if product not in pandigitals:
                    pandigitals.append(product)

print sum(pandigitals)

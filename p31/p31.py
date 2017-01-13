from numpy import convolve
import time

start = time.time()

pence = 200

coins = [1,2,5,10,20,50,100,200]

series = []

def makeGeneratingFxn(c):
    coEffs = []
    for i in range(pence+1):
        if i % c == 0:
            coEffs.append(1)
        else:
            coEffs.append(0)
    return coEffs

for coin in coins:
    series.append(makeGeneratingFxn(coin))



for s in range(len(series)):
    if s == 0:
        polynomial = series[s]
    else:
        polynomial = convolve(polynomial,series[s])

print polynomial[pence]
print("--- %s seconds ---" % (time.time() - start))

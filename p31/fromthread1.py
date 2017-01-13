an=[1]+[0]*200
fan=[1,2,5,10,20,50,100,200]

for i in fan:
    for j in range(i,201):
        an[j]+=an[j-i]

print an[200]

nNum = 600851475143
nDivideTry = 3
aFactors = []
while nNum > 1:
    while nNum % nDivideTry == 0:
        nNum = nNum/nDivideTry
        aFactors.append(nDivideTry)
    nDivideTry += 2
print (aFactors)

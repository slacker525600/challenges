nOne = 999
nTwo = 999
aPals = []
while nOne > 800:
    nTwo = 999
    while nTwo > 800:
        sString = str(nOne *nTwo)
        #print (sString)
        if(sString == sString[::-1]):
            aPals.append(sString)
        nTwo = nTwo -1
    nOne = nOne -1

print (aPals)

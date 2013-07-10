aPrimes = [2, 3, 5, 7, 11]
nNumCheck = 13
while len(aPrimes) < 10001:
    nNumChecking = nNumCheck
    for nPrime in aPrimes:
        while nNumCheck % nPrime ==0:
            nNumCheck = nNumCheck / nPrime

    if nNumCheck > 1:
        if nNumCheck != nNumChecking:
            break
        aPrimes.append(nNumCheck)
    nNumCheck = nNumChecking + 2

print (aPrimes)

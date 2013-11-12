nCount = 0
nRuns = 0 
for nToCheck in range(0,1000000):
  sTen = str(nToCheck)
  sTwo = bin(nToCheck)[2:]
  #print(sTen, sTwo)
  if sTen == sTen[::-1] and sTwo[:] == sTwo[::-1]:
    nCount += nToCheck
    print('is a palindrom: ',nToCheck)
  nRuns +=1
print(nRuns, nCount)

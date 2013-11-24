anPentagonal = []
nOn = 0
nPentOn = 0
nMinDifference = 1000000

nPentDif = 1
nNew = 1

while nMinDifference > nPentDif:
  #tests
  for nLower in anPentagonal[:nOn]:
    #print(anPentagonal)
    nDif = abs(nPentOn - nLower)
    nSum = abs(nPentOn + nLower)
    while anPentagonal[-1] < nSum:
      #get up to the sum, to check if it is pentagonal
      anPentagonal.append(nNew)
      nPentDif += 3 
      nNew += nPentDif

    if nDif in anPentagonal and nSum in anPentagonal:
      print('reached here, ', nDif)
      nMinDifference = min(nDif, nMinDifference)
  #always add one
  anPentagonal.append(nNew)
  nPentDif += 3 
  nNew += nPentDif

  nPentOn = anPentagonal[nOn]
  nOn += 1  
  #print(nOn, nPentOn, nPentDif)
  if nOn > 1000000:
    break

print(nMinDifference)
  


import math
anPentagonal = []
nOn = 0
while bUnFinished:
  nNew = n*(3*n -1)/2
  for nLower in anPentagonal:
    nDif = math.abs(nNew - nLower)
    nSum = math.abs(nNew + nLower)
    if nDif in anPentagonal:
      #want to check if sum is in ... but ... really just need to check if 
      nSum * 2 # ... uh ... == n (n*3 - 1) == n^2 *3 - n
  anPentagonal.append(nNew)
 
  


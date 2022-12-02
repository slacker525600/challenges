#have prime factorization in 21 along with divisors from prime factors
#not sure how often this code will be reused, just copying it in for this task
#will reorganize helper functions if repeats occur again. 

import math

def pfp(n):
    nOriginal = n
    anPrimeFactors = [1]
    nFactor = 3
    while n%2 == 0:
        n = n/2
        anPrimeFactors.append(2)
    while nFactor <= math.sqrt(nOriginal):
        while n%nFactor == 0:
            n= n/nFactor
            anPrimeFactors.append(nFactor)
        nFactor += 2
        if nFactor%3 == 0:
           nFactor += 2
    if n != 0:
        anPrimeFactors.append(n)
    return anPrimeFactors

def enum_divs(anPFs):
    #want to pick 1 of each, 2 3 .. until all, and all variants. 
    # this is a 2^n, but small sets in general, so not a big deal, 
    #print(anPFs)
    anToProc = [1] #anPFs[:]
    nCountThisFact = 1
    nFactOn = 0
    while nFactOn < len(anPFs):
      nFact = anPFs[nFactOn]
      nStart = len(anToProc) *(nCountThisFact-1)/nCountThisFact
      #print(nStart)
      for nMult in anToProc[nStart:]:
        anToProc.append(nMult*nFact)
      nFactOn += 1
      if nFactOn != len(anPFs):
        if nFact == anPFs[nFactOn]:
          nCountThisFact += 1
        else:
          nCountThisFact = 1

    #print(anToProc)
    anToReturn = []
    for nVal in anToProc:
        if not nVal in anToReturn:
            anToReturn.append(nVal)
    return anToReturn
def is_pos_sum(n, anVars):
  nSmall = 0
  nBig = len(anVars)-1
  while nSmall <= nBig:
    if anVars[nSmall] + anVars[nBig] == n:
        #print(n,anVars[nBig],anVars[nSmall])
        return True
    elif anVars[nSmall] + anVars[nBig] > n:
      nBig -= 1
      while nSmall > 0 and anVars[nSmall] + anVars[nBig] > n:
        nSmall -= 1
    else: 
      nSmall +=1 
  return False

nSum = sum(range(1,24)) #nothing smaller than 24 works
print(nSum)
anAbundant = [12,18,20]
for i in range(24, 28123):
  anFac = pfp(i)
  anDivs = enum_divs(anFac)
  anDivs= anDivs[:-1]#remove self from list.
  #print(i, anDivs, anFac)
  if not is_pos_sum(i,anAbundant):
    nSum += i
    #print('not possible ', i)
    if sum(anDivs) > i:
      print(i, 'not possible sum and abundant')
  if sum(anDivs) > i:
    anAbundant.append(i)
    #print('is abundant ',anAbundant)
#  if i > 300: 
#    break
print(nSum)

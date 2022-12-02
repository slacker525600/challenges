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

def is_prime(n):
  if n < 1 or math.floor(n) != n:
    raise ValueError
  bToReturn = True
  if n%2 ==0 and n != 2:
    bToReturn = False
  if bToReturn and n%3 == 0 and n != 3:
    bToReturn = False
  nFactor = 5
  while bToReturn and nFactor <= math.sqrt(n):
    if n%nFactor == 0:
      bToReturn = False
    nFactor += 2
    if nFactor%3 == 0:
      nFactor += 2
  return bToReturn

def test():
  for n in range(2,100):
    if len(pfp(n)) == 2 and not is_prime(n):
      print('error: ', n, pfp(n), is_prime(n))
print('2', is_prime(2))
#test() #fixed errors
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


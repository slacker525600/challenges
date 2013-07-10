#amicable numbers, 
#
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

#need to take pfp list and create list of divisors, 
#passing around lists of lists is a pain, 
# for len 1, list of all, for len 2, all 1s, * missing
def gen_subs_of_len(anPFs, i):
    aanToReturn = []
    if i == 0:
        aanToReturn = [1]
    elif i > len(anPFs):
        print('no subsets of length longer than array')
        return []
    else:
       for nVal in anPFs:
           anCopy = anPFs[:]
           anCopy.remove(nVal)
           aanToReturn.extend(map(lambda (x): x*nVal,gen_subs_of_len(anCopy, i-1)))
    return aanToReturn

def gen_subsets(anPFs):
    aanToReturn = anPFs[:]# all prime factors are factors by Default.
    
    for i in range(1, len(anPFs) - 1):
        anTemp = gen_subs_of_len(anPFs, i)
        print(anTemp)
        aanToReturn.extend(gen_subs_of_len(anPFs, i))
    return aanToReturn

def mult_array(anToMult):
    def mult(a,b): return a*b
    print(anToMult)
    return reduce(mult, anToMult,1)
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

nSum = 0 
for i in range(2,10003):
    anDivisors = enum_divs(pfp(i))
    #divisors includes self, 
    anDivisors= anDivisors[:-1]
    #print(i, anDivisors, sum(anDivisors))
    if sum(enum_divs(pfp(sum(anDivisors)))[:-1]) == i and i != sum(anDivisors):
        nSum += i
        print(nSum, i, sum(anDivisors))
    #if i > 20:
    #    break
print(nSum)
#print(pfp(989549731))
#

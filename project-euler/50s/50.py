import pfp
#should probably just pickly the list of the first million primes ... but whatever. 

anPrimes = pfp.gen_prime_list(1000000)
print(len(anPrimes))

#can I search the whole space, start at max, back away, contain smallest, while this is too big keep reducing
nMaxLen = len(anPrimes) - 1

nToCheck = sum(anPrimes[:nMaxLen])
while nToCheck > anPrimes[-1]:
  #nToCheck = sum(anPrimes[:nMaxLen])
  nToCheck -= anPrimes[nMaxLen]
  nMaxLen -= 1
print(nMaxLen, 'first check') #

bFound = False
for nLen in range(nMaxLen,22,-1):
  #all ranged of lengths starting at max
  for nStart in range(0, len(anPrimes) - nLen): #start to end window sized
    nToCheck = sum(anPrimes[nStart:nStart+nLen])
    #could use same -= trick as above to speed this up, but not important pretty small search spaces. 
    if nToCheck in anPrimes:
      print('new winner ', nToCheck, nLen)
      bFound = True
      break
    if nToCheck > anPrimes[-1]: #no reason to keep searching range once past a million
      break
  if bFound:
    break 
    
#pfp.add_primes(anPrimes, nUpTo)

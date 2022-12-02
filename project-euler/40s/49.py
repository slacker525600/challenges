#arithmetic sequence, 
#permutations
#all prime. 
import pfp

def get_digits_count_dict(nNumber):
  dnToReturn = {}
  while nNumber > 0:
    if dnToReturn.get(nNumber%10) != None:
      dnToReturn[nNumber%10] += 1
    else:
      dnToReturn[nNumber%10] = 1
    nNumber/=10
  return dnToReturn

def get_digits_array(nNumber):
  anToReturn = []
  while nNumber > 0:
    anToReturn.append(nNumber%10)
    nNumber/=10
  return anToReturn

def comp_digits(a,b,c):
  bToReturn = True

  dAsDigs = get_digits_count_dict(a)
  dBsDigs = get_digits_count_dict(b)
  dCsDigs = get_digits_count_dict(c)

  for nAKey , nAValue in dAsDigs.items():
    if dBsDigs.get(nAKey) == None or dCsDigs.get(nAKey) == None:
      bToReturn = False
      break
    if dBsDigs[nAKey] != nAValue or dCsDigs[nAKey] != nAValue:
      bToReturn = False
      break

  return bToReturn    
  
def test(a,b,c):
  bToReturn = True
  if not pfp.is_prime(a):
    bToReturn = False
  if bToReturn and not pfp.is_prime(b):
    bToReturn = False
  if bToReturn and not pfp.is_prime(c):
    bToReturn = False
  if bToReturn and c-b != b-a:
    bToReturn = False
  comp_digits(a,b,c)



#start by generating list of all primes, 
anPrimes = pfp.gen_prime_list(9999)
#print(len(anPrimes), anPrimes)
#find arithmatic 
while anPrimes[0] < 1000:
  anPrimes.remove(anPrimes[0])

for  nIndex, nPrime in enumerate(anPrimes):
  #print(nIndex, nPrime)
  for nPrimeTwo in anPrimes[nIndex + 1:]:
    if (nPrimeTwo + (nPrimeTwo - nPrime)) in anPrimes:
      #all three are primes
      if comp_digits(nPrime,nPrimeTwo, nPrimeTwo + (nPrimeTwo - nPrime)):
        print(nPrime,nPrimeTwo, nPrimeTwo + (nPrimeTwo - nPrime))



#sort of funny ... since arithmatic sequence ... 
#increase can't be odd or wont be primes, 
#needs to be divisibly by three because otherwise one of the additions would be
#... if adding 6 and 12 and ... one carry ... prevents permutation not enough entropy... 
# need to change at least 2 digits... for 1 change
#cant land on a 5 ... o + e + e ... 2 135 357 791 913  4 159 371 715 937   6 173 395 739 951  8  0  
#if addition ends in 2 start cant end in 1 3 4 cant start 1 7

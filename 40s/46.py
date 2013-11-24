import pfp

anPrimes = [2,3]

def add_primes(anPrimes, nUpTo):
  #should return a list with the next prime above nUpTo
  #adding two for ease, start prime list with 2,3
  nStart = anPrimes[-1]
  while anPrimes[-1] < nUpTo:
    nStart += 2
    bIsPrime = True
    for nPrime in anPrimes:
      if nStart%nPrime == 0:
        bIsPrime =False
        break
    if bIsPrime:
      anPrimes.append(nStart)
  return anPrimes

anSquares = [1,4,9,16]
def add_squares(anSquares,nUpTo):
  while anSquares[-1] < nUpTo:
    # dif of squares +2 is next dif, 
    anSquares.append(anSquares[-1] + (anSquares[-1] - anSquares[-2]) +2)
  return anSquares

def can(nOn, anPrimes, anSquares):
  #if nOn can be written as the sum of twice a square and a prime. 
  # do not know how to do this. without enumerating over two lists, so... enumerating. 
  # first things first, if an
  if anPrimes[-1] < nOn:
    anPrimes = add_primes(anPrimes,    nOn)
  bToReturn = False
  if anSquares[-1]< nOn:
    anSquares = add_squares(anSquares, nOn)
  for nSquare in anSquares:
    if (nOn - nSquare * 2) in anPrimes:
      bToReturn = True
      break 
  return bToReturn

def next_odd_composite(nOn):
  nOn += 2
  while pfp.is_prime(nOn):
    nOn +=2
  return nOn

nOn = 33
while can(nOn, anPrimes, anSquares):
  nOn = next_odd_composite(nOn)

print(nOn)

import pfp

nToCheck =11
anPossibleDigits = [1, 3, 7, 9]
def next_number(nNumber):
  nDigOn = 0
  bCarry = True
  while bCarry:
    bCarry = False
    nDigit = nNumber%10
    #print(nDigit,bCarry,nNumber,nDigOn)
    if nDigit == 9:
      bCarry = True
      nNumber -= 8* 10 ** nDigOn
    elif nDigit == 7 or nDigit == 1:
      nNumber += 2 * 10 ** nDigOn
    elif nDigit == 3:
      nNumber += 4* 10 ** nDigOn
    nDigOn += 1
  return nNumber

def check_truncation(nNum):
  anDigits = []
  anToCheck = []
  nExponent = 0
  nGrowing = 0

  while nNum > 0:
     anToCheck.append(nNum)
     nGrowing = nGrowing + (nNum %10)*(10**nExponent)
     anToCheck.append(nGrowing)
     #anToCheck.append( sum( map( lambda(x): anDigits.append( nNum%10 ))))
     nNum/=10
     nExponent += 1

  bToReturn = True
  for nToCheck in anToCheck:
    if not pfp.is_prime(nToCheck) or nToCheck == 1:
      bToReturn = False

  return bToReturn

print('check', check_truncation(23))

anFound = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
#found answers already, 
nInc = 9 ##single digits arent truncatable.
while len(anFound) < 11:

  nToCheck = next_number(nToCheck)
  #print(nToCheck)
  if pfp.is_prime(nToCheck) :
    if check_truncation(nToCheck):

      anFound.append(nToCheck)
      print(anFound)
  nInc += 2

print(sum(anFound))

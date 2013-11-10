import pfp

def rotate(nToRotate):
  nLen = 10
  while nToRotate/nLen:
    nLen *= 10
  return nToRotate/10 + (nToRotate%10)*nLen/10

def check_circle(nToCheck):
  bToReturn = True
  nRotating = rotate(nToCheck[-1])
  while bToReturn and nRotating != nToCheck[-1]:
    if len(pfp.pfp(nRotating)) > 2:
      bToReturn = False
    nRotating = rotate(nRotating)
  return bToReturn

#print(pfp.pfp(34234))
nCount = 1 #starting with 2, even special case. 
for nToCheck in range(2,1000000):#1000000):
  anFactors = pfp.pfp(nToCheck)
  if len(anFactors) == 2:
    if(check_circle(anFactors)):
      print(nToCheck)
      nCount +=1
    nToCheck += 1
print(nCount)

import pfp

def my_distinct(aanFactors):
  dDict = {}
  bFail = False
  for anFact in aanFactors:
    for nFact in anFact:
      #this may break, but can convert to string... slow but ... effective?
      if dDict.get(str(nFact)) != None:
        bFail = True
        break
      else:
        dDict[str(nFact)] = True
    if bFail:
      break
  return not bFail

def convert(anPrimeFactors):
  anToReturn = []
  #init
  anToReturn.append([anPrimeFactors[0], 1])
  anPrimeFactors.remove(anToReturn[0][0])
  while len( anPrimeFactors) > 0:
    if (anToReturn[-1][0] == anPrimeFactors[0]):
      anToReturn[-1][1] += 1 
    else:
      anToReturn.append([anPrimeFactors[0],1])
    anPrimeFactors.remove(anPrimeFactors[0])
  return anToReturn

nOn = 4
aanFactors = [[[2,1]],[[3,1]],[[2,2]],[[5,1]]]
nFactors = 4 #looking for example 

def check(aanFactors):
  bToReturn = True
  for anFact in aanFactors:
    if len(anFact) != nFactors:
      bToReturn = False
  if bToReturn :
    bToReturn = my_distinct(aanFactors)
  return bToReturn

while not check(aanFactors): 
#len(aanFactors[0]) != nFactors or len(aanFactors[1]) != nFactors or \
#      len(aanFactors[2]) != nFactors or len(aanFactors[3]) != nFactors  or not my_distinct(aanFactors):
  nOn += 1
  aanFactors = aanFactors[1:]
  aanFactors.append(convert(pfp.pfp(nOn)))
  #print(aanFactors)
  #if nOn > 7000:
  #  break
print(nOn)

#pandigital numbers
# reminds me of that doctor who joke, nobody does recreational mathematics anymore ... friendly numbers ha
# n-digit number is pandigital if it makes use of all the digits 1 to n
# looking for all x * y = n where xyn is 9 digit pandigital 
# and then sum all the ns, not repeating any, 
# n's range is relatively small, as x*y =n needs to be 9 digits, 
# so, x + y need to be 5 or fewer digits for n to be 4 or fewer
# and if x and y are both 2 digits, n cant be 5 digits 99*99 < 10000
# so ... x and y need to total 5 digits and n needs to be 4 digits, limits the range quite a bit. 

def is_pan(nA,nB,nC):
  bToReturn = True
  dDict = {}
  while nA >0 and bToReturn:
    if dDict.get(str(nA%10)):
      bToReturn = False
      #print('break')
      break
    else:
      dDict[str(nA%10)] = True
    nA /=10
  while nB >0 and bToReturn:
    if dDict.get(str(nB%10)):
      bToReturn = False
      #print('you')
      break
    else:
      dDict[str(nB%10)] = True
    nB /=10
  while nC >0 and bToReturn:
    if dDict.get(str(nC%10)):
      bToReturn = False
      #print('do')
      break
    else:
      dDict[str(nC%10)] = True
    nC /=10
  dDigits = ['1','2','3','4','5','6','7','8','9']
  #print(dDict)
  for sVal in dDigits:
    if not dDict.get(sVal):
      #print('here false')
      bToReturn = False
  return bToReturn

#print(is_pan(1,2,3))
#print(is_pan(12,2,3))
#print(is_pan(14567890,2,3))

aanSolutions = []
for x in range(2,100):
  for y in range(2,10000):
    n = x*y 
    if not n >= 10000:
      if is_pan(x,y,n):
        aanSolutions.append([x,y,n])
nSum = 0
dDict = {}
for anSolution in aanSolutions:
  if not dDict.get(str(anSolution[-1])):
    dDict[str(anSolution[-1])] = True
    nSum += anSolution[-1]
  else:
    print('repeats', anSolution[-1])
print(nSum)
#did something wrong ... oh 0 shouldnt be included
#print(is_pan(39, 186, 7254))

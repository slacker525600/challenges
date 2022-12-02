#number of ways of creating 200 with set [1, 2, 5, 10, 20, 50,100,200]
def sum_ar_mult(anA, anB):
  return sum([a*b for a,b in zip(anA,anB)])

def solve_array(nTarget, nLocToDec, anArray, anCoins):
  #anArray[nLocToDec] -= 1 
  nLocToUp = nLocToDec + 1
  while sum_ar_mult(anArray, anCoins) != nTarget:
    nSum = sum_ar_mult(anArray, anCoins)
    #need to increment progressively.
    anArray[nLocToUp] = (nTarget - nSum) / anCoins[nLocToUp] #this sets the location to a max value
    nLocToUp += 1 
    if nLocToUp == len(anArray) and sum_ar_mult(anArray, anCoins) != nTarget:
      print("something is wrong, last cell should be the finisher regardless, because should always be divis by 1")
      break
  return anArray

#why is this problem hard
# back and forth 
# decrease
anCoins = [200,100,50,20,10,5,2,1]
aanSolutions = []
nTarget = 200
anPosSolution = [0,0,0,0,0,0,0,0]

nPosToInc = 0 #this is the currently maximizing location, will also be the decrementing location on next guess.
while anPosSolution[-1] != nTarget: #last possible answer is 200 pennies
  #set max for this loc. actually set one above, so loop decrement will just work
  anPosSolution[nPosToInc] = nTarget / anCoins[nPosToInc]
  nPosToDec = nPosToInc
  while anPosSolution[nPosToInc] > 0:
    ##start with max at left, then 0 from right, until you reach the pos you are decrementing, then decrement one, and again max from left
    #0 pennies, go left decrement first available
    anPosSolution = solve_array(nTarget, nPosToDec, anPosSolution, anCoins ) 
    #print('here',nTarget, nPosToInc, anPosSolution, anCoins)
    aanSolutions.append(anPosSolution[:])
    if sum(anPosSolution) == anPosSolution[-1]:
      #end edge case
      break
    anPosSolution[-1] = 0
    nEnd = len(anPosSolution) - 1
    while nEnd >= nPosToInc:
      if anPosSolution[nEnd] > 0:
        anPosSolution[nEnd] -= 1
        nPosToDec = nEnd
        break
      nEnd -= 1
  nPosToInc += 1
for anSolution in aanSolutions:
  print(anSolution)
print(len(aanSolutions))

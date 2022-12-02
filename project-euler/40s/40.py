#this appears to be another that can be done by hand. 
#digits of natural numbers
# want 1*10*100*1000*10000*100000*1000000
# first digit is 1. 10th is the 1 of 10. 
# 100th ... is 90 later... which is 45 numbers later since first 10-99 have 2
#


nDig = 0
anNumberOn = [1]
dToFind = { 1:True,10:True,100:True,1000:True,10000:True,100000:True,1000000:True }
nMultiply = 1
while nDig <= 1000000:
  #print(anNumberOn)
  for nDigit in anNumberOn[::-1]:
    nDig += 1
    if dToFind.get(nDig):
      nMultiply *= nDigit
      print(nDig, nDigit, anNumberOn)
      dToFind[nDig] = [nDigit, anNumberOn]
  #nDig += len(anSep)
  anNumberOn[0] += 1
  nCarryOn = 0
  while anNumberOn[nCarryOn] == 10:
    anNumberOn[nCarryOn] = 0 
    if nCarryOn + 1 == len(anNumberOn):  
      anNumberOn.append(1) 
    else: 
      nCarryOn += 1
      anNumberOn[nCarryOn] += 1
print(dToFind)
print(nMultiply)
  

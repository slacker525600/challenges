import math
#aanRatios = []

#{20,48,52}, {24,45,51}, {30,40,50}
# 5 12 13    8 15 17     3 4 5 
#looking for perimeter with most 
#a+b+c = p and a^2 +b^2 = c^2
nMaxCount = 0
nIndex = -1

dAnswers = {}
for p in range(2,1000):
  h = p/2
  b = p/2
  a = 0
  nCount = 0
  while b >= a:
    b -= 1
    
    a = math.sqrt(h**2 - b**2)
    if a == math.floor(a):
      if not dAnswers.get(a+b+h):
        dAnswers[a+b+h] = 0
      dAnswers[a+b+h] += 1
aanToSort = []
for key,value in dAnswers.items():
  #print(key,value)
  aanToSort.append([key,value])
aanToSort.sort(key=lambda(a):a[1])
print(aanToSort[-1])


#and other approaches I chose not to take
sCodeToGetRats = """
nAdj = 1
nOpp = 1

while nAdj < 400:
  nOpp = nAdj
  while nOpp < 400:
    fHyp = math.sqrt(nAdj**2 + nOpp**2)

    if math.floor(fHyp) == fHyp:
      #is an integer, 
      for anRatio in anExistingRatios:
        
    nOpp += 1
"""


sNonCode = """
a = 1
b = 
c = math.sqrt(a**2 + b**2)

while a + b + c < 1000:
  b -= 1

perimeter = a + b + c
a + b > c
c + b > a
a + c > b
"""

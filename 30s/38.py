anDigits = [1,2,3,4,5,6,7,8,9]
nStart = 9361
while nStart > 9182:
  anToRemove = anDigits[:]
  nToCheck = nStart*(10**5) + nStart*2
  while nToCheck > 0:
    if anToRemove.count(nToCheck%10) == 1:
      anToRemove.remove(nToCheck%10)
    else:
      break
    nToCheck /=10
  if len(anToRemove) == 0:
    print(nStart*(10**5) + nStart*2,' pandigital from', nStart, [1,2]) 
  nStart -= 1 
sSamples = """
def sds():
  nNext =
  while 
  return nNext
[9,9,9,9,9,9,9,9,9]
nFirst = 987654321
#sort of think I can just do this by hand?

(1,2)
95> 9... 19
948 18 
947 18934
>=5 945 189
944 188
943 188  
936x 1872y 45 left, no worky
9
932718654

8719 17438
1   2    3
95>->190 
94 188
93 186 279 
92 184 276
91 182 273

1  2  3  4  
9 18 27 36 
91 182 273 364 more than 9 dig

1  2  3  4  5 
9 18 27 36 45

1 2 3 4 5 6 
9 more than 9 digits 
"""

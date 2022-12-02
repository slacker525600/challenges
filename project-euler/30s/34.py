#
import math
#362880 = 9 factorial
#print(math.factorial(9))
anDigitFactorials = [1,1,2,6,24,120,720,5040,40320,362880]
#145 is a solution
#print(math.factorial(9) * 7) #7 digit number
#sanity check that those values were right.
# and if I had started this at 0 ... I would have found my error way faster. 
#for n in range(1,len(anDigitFactorials)):
#  print(math.factorial(n), anDigitFactorials[n])

def dig_fact_sum(nToSum):
  nToReturn = 0
  while nToSum >0:
    nToReturn += anDigitFactorials[nToSum%10]
    nToSum /= 10
  return nToReturn

#brute force
nTotal = 0
for n in range(1,9999999):
  nResult = dig_fact_sum(n)
  #print(n, nResult)
  if n == nResult:
    nTotal += n
    #print(n)
#this is only giving me the one answer they already provided. 145 ... 
#... and thats because I was saying 0! == 0 which is a stupid thing to do... 0! = 1 damnit definitional issues
print( nTotal) 

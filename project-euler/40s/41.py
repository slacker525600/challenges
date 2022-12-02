import pfp 
import enum_pan_digital

#using array of digits over number for ease of setting up next  
anDigits = [9,8,7,6,5,4,3,2,1] #digits from least significant to most.
nCount =0 #debugging number of times through loop checking that next works
nLen = 9
while True:
  #smallest possible ... 
  nToCheck = sum(map(lambda (nIndex, nElement): nElement*(10**(len(anDigits) - 1 - nIndex)), enumerate(anDigits))) 
  #if len(anDigits) != nLen:
  #  print(nToCheck)
  if nToCheck == 2143:
    print('should be prime')
  if pfp.is_prime(nToCheck):
    print(nToCheck)
    break
  else:
    #print(anDigits)
    anDigits = enum_pan_digital.enum_pan_digital(anDigits)
    #print(anDigits)
  #if nCount > 500000:
  #  break
  #nCount += 1
  

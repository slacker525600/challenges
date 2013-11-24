#once again, an increment pandigital numbers, this time starting ten digit. 
#matching criteria
#d4 is even
#d3+d4+d5 %3 = 0
#d6 = 5 or 0
#d5d6d7 %7 == 0
#d6d7d8 %11 == 0 ... d6+d8 - d7 = 0 or 11 ?
#d7d8d9 %13 == 0
#d8d9d10 %17 == 0 
import pfp
import enum_pan_digital

def do_test(anDigits):
  if(len(anDigits) != 10):
    print('something horribly wrong')
  bToReturn = True
  if bToReturn and anDigits[3] % 2 != 0:
    bToReturn = False
  if bToReturn and (anDigits[2]*100 + anDigits[3]*10 + anDigits[4])%3 != 0:
    bToReturn = False
  if bToReturn and (anDigits[5])%5 != 0:
    bToReturn = False
  if bToReturn and (anDigits[4]*100 + anDigits[5]*10 + anDigits[6])%7 != 0:
    bToReturn = False
  if bToReturn and (anDigits[5]*100 + anDigits[6]*10 + anDigits[7])%11 != 0:
    bToReturn = False
  if bToReturn and (anDigits[6]*100 + anDigits[7]*10 + anDigits[8])%13 != 0:
    bToReturn = False
  if bToReturn and (anDigits[7]*100 + anDigits[8]*10 + anDigits[9])%17 != 0:
    bToReturn = False

  return bToReturn

anDigits = [9,8,7,6,5,4,3,2,1,0]
nSum = 0

while anDigits != [0,1,2,3,4,5,6,7,8,9]:
  anDigits = enum_pan_digital.enum_pan_digital(anDigits)
  if do_test(anDigits):
    nSum += sum(map(lambda (nIndex, nElement): nElement*(10**(len(anDigits) - 1 - nIndex)), enumerate(anDigits)))
print(nSum)

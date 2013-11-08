#trick to this question is first find all the digits to the fifth power. 
#going to test logic and resolve example first, see run time ... if there are issue etc

#def fourth_powers():
#  return [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]
#  return [i**4 for i in range(10)]
#print(fourth_powers())

def dig_sum(nToSum, anDigPowers):
  nCalculated = 0
  while nToSum > 0:
    nCalculated += anDigPowers[nToSum %10]
    nToSum /= 10
  return nCalculated

#anFourthPowers = fourth_powers()
#for n in range(9999):
#  if dig_sum(n,anFourthPowers) == n:
#    print(n)  

def fifth_powers():
  #always returns [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049] so 
  return [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]
  return [i**5 for i in range(10)]

#finding largest number to check for this, 
#n = 1
#while 10**n < n* 59049:
#  n += 1 
#print(n)

anPowers = fifth_powers()
anSolutions = []
for n in range(1000000):
  if dig_sum(n,anPowers) == n:
    print(n)
    anSolutions.append(n)

print(sum(anSolutions) -1 ) # 1 is not a sum and thus not a solution. despite meeting criteria outlined


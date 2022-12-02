#last ten digits of sum of 1 -1000 n^n
#only need to track ten digits. 
nMod = 10000000000
nSum = 0
for n in range(1,1001):
  nSum += n**n
  nSum = nSum % nMod
print(nSum)

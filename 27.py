#need pfp again, pulling it out, putting it into a file and 
import pfp 
#pfp  appears to be too slow? ... brute force strat ?

#print(pfp.pfp(79))
#n^2 + an + b where |a| <1000 and |b| < 1000
#if b is even, fail, n=2 even b div by 2, 
#also true of a,
nMax = 0
nA = 1
nB = 41
for a in range(-999,999,2):
 for b in range(-999,999,2):
   if a%3 ==0 and b %3 == 0:
      continue
   nConsPrime =0
   for i in range(0,1000):
     nTest = abs(i*i + a*i + b)
     anPFs = pfp.pfp(nTest)
     if len(anPFs) >2:
       break
     nConsPrime += 1
   if nConsPrime > nMax:
     print(a,b, nConsPrime)
     nMax = nConsPrime
     nA = a
     nB = b
#   if b > -975:
#     break
# if a > -975:
#   break

print(nA, nB, nMax)

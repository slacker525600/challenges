#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#F13 = 233


def naive_fib(n):
 if n ==0:
   return 1
 elif n ==1:
   return 1
 else:
   return fib(n-1) + fib(n-2)
def fib_help(n, anFib):
  if len(anFib) >= n:
    return anFib
  else:
    anFib.append(anFib[-1]+anFib[-2])
    return fib_help(n, anFib)
def fib(n):
  return fib_help(n,[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040])

#screw looking for anything interesting 
#print(fib(800))
import math
nBiggie = 1#math.pow(10,1000)
def fib_inc(a,b):
  if a > nBiggie:
    return [a,b]
  else:
    return fib_inc(b, a+b)
#3000 levels of recursion probably not the best move, 
#print(nBiggie)
#quit()
def add_array(a,b):
  anToReturn = [0]*len(a)
  nCarry= 0
  for i in range(0,len(a)):
    anToReturn[i] = a[i] + b[i] + nCarry
    if anToReturn[i] > 9:
      anToReturn[i] -= 10
      nCarry = 1
    else:
      nCarry = 0
  return anToReturn
def array_to_str(a):
  a = map(lambda x: str(x), a)
  sToPrint = ""
  n = 0
  bStarted = False
  while n < len(a):
    if not bStarted and a[len(a)-n-1] != '0':
      bStarted = True
    if bStarted:
      sToPrint +=  a[len(a)-n-1]
    n += 1
  return sToPrint
def print_array(a):
  print(array_to_str(a))
  return

nCounter =1
a = [0]*1000
b = [0]*1000
a[0] = 1#1
b[0] = 1#2
while a[999] == 0 and nCounter < 10000:
  temp = add_array(a,b)#first run 3 #trying to figure the counter starting loc
  #print(array_to_str(a), array_to_str(b), array_to_str(temp))
  a=b
  b=temp
  nCounter += 1
print_array(a)
print_array(b)
print(nCounter)
#
#1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816

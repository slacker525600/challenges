def repeat_len(n):
  nRemainder = 1
  anRemList = []
  while not nRemainder in anRemList:
    #print(n, nRemainder, anRemList)
    if nRemainder < n:
      anRemList.append(nRemainder)
      nRemainder *=10
    else:
      while n <= nRemainder:
        nRemainder -= n
    #print(n, nRemainder, anRemList)
  return len(anRemList) - anRemList.index(nRemainder)

for n in range(1,1000):
  print(n, ":", repeat_len(n))

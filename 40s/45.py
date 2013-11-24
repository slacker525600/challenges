#realization that all I need to do is keep two of each around. 

def build_next(nLast,nOn, nGetTo,nType):
  while nGetTo > nOn:
    nTemp = nOn + (nOn - nLast + nType )
    nLast = nOn
    nOn = nTemp
  return [nLast, nOn]

nTriType = 1
nPentType= 3
nHexType = 4

nTriLast = 1
nTriOn   = 3

nPentLast= 1
nPentOn  = 5

nHexLast = 1
nHexOn   = 6

nGetTo = 7

while nTriOn != nHexOn or nPentOn != nHexOn or nGetTo <= 40755:
  nGetTo = nHexOn + 1
  [nHexLast,  nHexOn]  = build_next(nHexLast, nHexOn, nGetTo, nHexType)
  nGetTo = nHexOn
  [nTriLast,  nTriOn]  = build_next(nTriLast, nTriOn, nGetTo, nTriType)
  [nPentLast, nPentOn] = build_next(nPentLast,nPentOn,nGetTo, nPentType)

print(nPentOn)

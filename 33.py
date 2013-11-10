asDigits = ['1','2','3','4','5','6','7','8','9']
aasNumbers = []
for sTopLeft in asDigits:
  for sTopRight in asDigits:
    for sBottomLeft in asDigits:
      for sBottomRight in asDigits:
        fToComp = 0
        if sTopLeft == sBottomLeft: 
          fToComp = float(sTopRight) /float(sBottomRight)
        elif sTopLeft == sBottomRight:
          fToComp = float(sTopRight) /float(sBottomLeft)
        elif sTopRight == sBottomLeft:
          fToComp = float(sTopLeft) /float(sBottomRight)
        elif sTopRight == sBottomRight:
          fToComp = float(sTopLeft) /float(sBottomLeft)
        fFrac = float(sTopLeft +sTopRight) / float(sBottomLeft + sBottomRight)
        if sTopLeft + sTopRight == sBottomLeft + sBottomRight:
          continue
        if fToComp == fFrac:
          #print(sTopLeft +sTopRight, sBottomLeft + sBottomRight)
          aasNumbers.append([sTopLeft +sTopRight, sBottomLeft + sBottomRight])

nTop = 1
nBottom = 1
for asNumbers in aasNumbers[:len(aasNumbers)/2]: # above does inverses above 0
  nTop = nTop *int(asNumbers[0])
  nBottom = nBottom * int(asNumbers[1])
  print(asNumbers[0], asNumbers[1])
print(nTop)
print(nBottom)

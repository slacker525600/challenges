def enum_pan_digital(anCurrent):
  anEnd = []
  #print(anCurrent)
  while len(anCurrent) > 0:
    if len(anEnd) > 0:
      if anCurrent[-1] < anEnd[-1]:
        anEnd.append(anCurrent[-1])
        anCurrent.remove(anEnd[-1])
      else:
        break
    else:
      #base case, get element to compare
      anEnd.append(anCurrent[-1])
      anCurrent.remove(anEnd[-1])
  if len(anCurrent) == 0:
    #fill nCurrent, with all but first digit of end. 
    print(anEnd)
    anEnd = anEnd[1:] #remove largest digit. ie going to an 8 digit pan digital from 9 remove 9
    while len(anEnd) > 0:
      anCurrent.append(anEnd[0])
      anEnd.remove(anEnd[0])
    print('dropping a digit', anCurrent)
    return anCurrent
  #now have an array with the end sorted, need to decrement the end digit of anCurrent
  nDigOn = 0 
  nToDec = anCurrent[-1]
  anCurrent.remove(nToDec)
  while nDigOn < len(anEnd) and nToDec < anEnd[nDigOn]:
    #find next smallest in order to decrement
    nDigOn += 1
  # found next smallest, decrementing digit on, then go largest to smallest 
  anCurrent.append(anEnd[nDigOn])
  anEnd.remove(anEnd[nDigOn])
  #if nothing to append, just append the digit just decremented
  bInserted = False
  if len(anEnd) == 0:
    anCurrent.append(nToDec)
    bInserted = True
  while len(anEnd) > 0:
    #else while there are digits to append, go max to min anEnd is sorted by definition, where does nToDec go
    if (anEnd[0] < nToDec) and not bInserted:
      #print('got here')
      anCurrent.append(nToDec)
      bInserted = True
    anCurrent.append(anEnd[0])
    anEnd.remove(anEnd[0])
  if not bInserted:
    anCurrent.append(nToDec)
  return anCurrent
  
def test():
  anToDec = [4,3,2,1]
  sOldTests = """
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)"""
  anToDec = [9,8,7,6,3,1,2,4,5]  
  anToDec = enum_pan_digital(anToDec)
  print(anToDec)
#test()


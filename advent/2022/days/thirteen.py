from days.generic import GenericProc

testInput = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

state = {
  'pairOn': 1,
  'left': None,
  'correctPairs': [],
  'orderedLines': []
}

def compareArrays(left, right, final=False):
  '''If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
'''
  if type(left) != type([]):
    left = [left]
  if type(right) != type([]):
    right = [right]
  # print('starting compare', left, right)
  i = 0
  toReturn = 0
  while i < len(left) and toReturn == 0:
    ## print(i)
    if(len(right) == i):
      # we've exhausted items on the right, so we quit and return false
      # print('False exhausted')
      toReturn = -1
    elif type(left[i]) == type(1) and type(right[i]) == type(1):
      if left[i] < right[i]:
        # print('True left < right', left[i], right[i])
        toReturn = 1
      elif right[i] < left[i]:
        # print('False left > right', left[i], right[i])        
        toReturn = -1
    else:
      # print('recursive call left', left[i], 'right',right[i])
      toReturn = compareArrays(left[i],right[i])
    i += 1
  if (toReturn == 0 and len(left) < len(right)):
    toReturn = 1
    # print('True exhausted left before right')
  # # # print('wtf?', final, toReturn)
  # if final and toReturn == 0:
  #   # print('True bail with default', left, right)
  # elif toReturn == 0:
  #   # print('continue exhausted', left, right)
  # elif toReturn == -1:
  #   # print('False found', left, right)
  # elif toReturn == 1:
  #   # print('True found', left, right)

  return True if final and (toReturn == 1 or toReturn == 0) else (False if (final and toReturn == -1) else toReturn)
# 4337 - 6671

def lineLambda(state, line):
  if line:
    value = eval(line)
    if state['left'] is None:
      state['left'] = value
    else:
      # now we can compare the line we are on against the last one, 
      # print('comparing', state['left'], value)
      if compareArrays(state['left'], value, final=True):
        # print('correct order')
        state['correctPairs'].append(state['pairOn'])
      # else:
        # print('incorrect order')
      state['left'] = None
    
    for index, orderedVal in enumerate(state['orderedLines']):
      correctOrder = compareArrays(orderedVal, value, final=True)
      if index == len(state['orderedLines']) -1 and correctOrder:
        state['orderedLines'].insert(index, value)
        break
      elif correctOrder:
        continue
      else:
        # incorrect order insert before this thing
        state['orderedLines'].insert(index, value)
        break

    if not state['orderedLines']:
      # if this was the first line, above loop doesn't do anything
      state['orderedLines'].append(value)
  else: 
    state['pairOn'] += 1
  return state


def partOneSummary(state):
  # print(state, sum(state['correctPairs']))
  return sum(state['correctPairs'])

def partTwoSummary(state):

  twoControlIndex = -1
  sixControlIndex = -1
  # print(state['orderedLines'])
  for index, orderedVal in enumerate(state['orderedLines']):
    correctOrder = compareArrays(orderedVal, [[2]], final=True)
    if index == len(state['orderedLines']) -1 and correctOrder:
      state['orderedLines'].insert(index, [[2]])
      twoControlIndex = index
      break
    elif correctOrder:
      continue
    else:
      # incorrect order insert before this thing
      state['orderedLines'].insert(index, [[2]])
      twoControlIndex = index
      break

  for index, orderedVal in enumerate(state['orderedLines']):
    correctOrder = compareArrays(orderedVal, [[6]], final=True)
    if index == len(state['orderedLines']) -1 and correctOrder:
      state['orderedLines'].insert(index, [[6]])
      sixControlIndex = index
      break
    elif correctOrder:
      continue
    else:
      # incorrect order insert before this thing
      state['orderedLines'].insert(index, [[6]])
      sixControlIndex = index
      break
  print(state['orderedLines'])    
  # print(sixControlIndex * twoControlIndex, sixControlIndex , twoControlIndex)
  # 0 vs 1 indexing and index before insert is below value where it ends up, so plus two 
  return (sixControlIndex +2) * (twoControlIndex +2)
  
thirteen = GenericProc('days/day13input.txt', state, lineLambda, partOneSummary, testInput, 13)
thirteen.test()
print(thirteen.run())

thirteenTwo = GenericProc('days/day13input.txt', state, lineLambda, partTwoSummary, testInput, 140)
thirteenTwo.test()
print(thirteenTwo.run())


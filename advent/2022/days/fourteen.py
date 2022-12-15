from days.generic import GenericProc

testInput = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

# some lines making a grid, sand will fall in a single grain at a time, rules for sand coming to rest, or falling out past the lines 

state = {
  'grid': [],
  'minX': None,
  'maxX': None,
}

# grid coordinates ... min/max x val and depth append . to begin and end
def displayGrid(state):
  print(str(state['minX']) + ' '*5* (int(state['maxX'] or 0 )- int(state['minX'] or 0)) + str(state['maxX']))
  for index, row in enumerate(state['grid']):
    print(index, row)

def lineLambda(state, line):
  displayGrid(state)
  points = line.split('->')
  points = list(map(lambda x: (int(x.split(',')[0]),int(x.split(',')[1])), points))

  # determine bounds to compare against existing grid
  minX = min(map(lambda x: x[0], points))
  maxX = max(map(lambda x: x[0], points))
  maxY = max(map(lambda x: x[1], points))
  # now that we have the bounds of these lines, min y is 0 max y is len grid, x min/max are in state
  
  # initialize state from first line with maxY arrays of '.' of maxX -minX size
  if not state['grid']:
    for y in range(0, maxY+1):
      state['grid'].append(['.'] * (maxX -minX + 1))
    state['minX'] = minX
    state['maxX'] = maxX

  # append leading . arrays of len state['minX'] - minX 
  if minX < state['minX']:
    for rowIndex in range(0, len(state['grid'])):
      temp = (['.']*(state['minX'] - minX))
      temp.extend(state['grid'][rowIndex])
      state['grid'][rowIndex] = temp
    state['minX'] = minX

  # append following . arrays of len maxX - state['minX']
  if maxX > state['maxX']:
    for rowIndex in range(0, len(state['grid'])):
      state['grid'][rowIndex].extend((['.']*(maxX -state['maxX'])))
    state['maxX'] = maxX
  
  while maxY + 1 > len(state['grid']):
    state['grid'].append(['.']*(len(state['grid'][-1])))

  # then draw the lines 
  pointIndex = 0
  while pointIndex < len(points) - 1:   # last point doesn't connect a line to a new point
    (fromX, fromY) = points[pointIndex]
    (toX, toY) = points[pointIndex+1]
    # vertical segments replace grid at x index from y start to y finish 
    # horizontal segments replace grid at y row from x start to x finish 
    if fromX == toX:
      # x same means vertical line
      minY = min([fromY, toY])
      maxY = max([fromY, toY])
      for y in range(minY, maxY+1):
        state['grid'][y][toX - state['minX']] = '#'
    elif fromY == toY:
      # y same means horizontal line 
      minX = min([fromX, toX])
      maxX = max([fromX, toX])
      for x in range(minX, maxX+1):
        state['grid'][fromY][x - state['minX']] = '#'
    else:
      print('Horribly wrong diagonal line')
      # diagonal line? 
    pointIndex += 1
  return state

def dropSand(state, sandTarget): # -> (landed bool, took grains):
  rowLen = len(state['grid'][0])

  if (sandTarget[0] - state['minX']) not in range(0, rowLen) or sandTarget[1] < 0 or sandTarget [1] >= len(state['grid']):
    return 0, 0
  elif state['grid'][sandTarget[1]][sandTarget[0]-state['minX']] != '.':
    return 1, 0

  t0, t1, t2, t3 = 0,0,0,0
  t1x, t1y = sandTarget[0] - state['minX'],   sandTarget[1] + 1
  t2x, t2y = sandTarget[0] - state['minX']-1, sandTarget[1] + 1
  t3x, t3y = sandTarget[0] - state['minX']+1, sandTarget[1] + 1

  filled2, filled3 = 0,0

  landed1, filled1 = dropSand(state, (t1x+state['minX'], t1y))
  if landed1:
    landed2, filled2 = dropSand(state, (t2x+state['minX'], t2y))
    if landed2:
      landed3, filled3 = dropSand(state, (t3x+state['minX'], t3y))

  if t1x>=0 and t1x < rowLen and state['grid'][t1y][t1x] != '.' and \
     t2x>=0 and t2x < rowLen and state['grid'][t2y][t2x] != '.' and \
     t3x>=0 and t3x < rowLen and state['grid'][t3y][t3x] != '.' and \
      state['grid'][sandTarget[1]][sandTarget[0] - state['minX']] == '.':
    state['grid'][sandTarget[1]][sandTarget[0] - state['minX']] = 'O'
    t0 = 1

  return t0, (t0+filled1+filled2+filled3) 

def partOneSummary(state):
  displayGrid(state)
  # keep putting falling object at 500,0 until it falls out the grid
  sand, sum = dropSand(state, (500,0))
  print(sum)
  return sum

def addBase(state):
  # want to add a neverending base 1 layer below the lowest level now 
  maxDistCenter = len(state['grid']) +2
  minX = 500 - maxDistCenter - 2 # just adding buffer because why
  maxX = 500 + maxDistCenter + 2
  y = len(state['grid']) + 1
  state = lineLambda(state, f'{minX},{y} -> {maxX},{y}')

def partTwoSummary(state):
  displayGrid(state)
  addBase(state)
  displayGrid(state)

  # keep putting falling object at 500,0 until it falls out the grid
  sand, sum = dropSand(state, (500,0))
  displayGrid(state)
  print(sum)
  return sum
  
fourteen = GenericProc('day14input.txt', state, lineLambda, partOneSummary, testInput, 24)
fourteen.test()
print(fourteen.run())

fourteenTwo = GenericProc('day14input.txt', state, lineLambda, partTwoSummary, testInput, 93)
fourteenTwo.test()
print(fourteenTwo.run())


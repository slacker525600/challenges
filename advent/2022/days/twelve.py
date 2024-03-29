import copy

from days.generic import GenericProc

testInput = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

state = {
  'grid': [],
  'distGrid': [],
  'endLoc': (-1,-1),
  'startingLocations': [],
  'startLoc': ()
}

# thinking load the full grid, create distance grid of same size filled with -1 except for 0 at S loop until E has a value
# while loc of E == -1 
# find all locs with val = n 
# mark all -1 cells that are adjacent with n + 1 
def heightFrom(char):
  if ord(char) >= ord('a') and ord(char) <= ord('z'):
    return ord(char) - ord('a') + 1
  if char == 'S':
    return 1
  if char == 'E':
    return 26
  return char

def lineLambda(state, line):
  state['grid'].append(list(map(heightFrom, list(line))))
  state['distGrid'].append(list(map(lambda x: -1, list(line))))
  if 'S' in line:
    state['startLoc'] = (line.index('S'),len(state['grid'])-1)
    state['startingLocations'].append((line.index('S'),len(state['grid'])-1))
  if 'E' in line:
    state['endLoc'] = (line.index('E'), len(state['grid'])-1)
  if 'a' in line:
    locations = [i for i, ltr in enumerate(line) if ltr == 'a']
    state['startingLocations'].extend(list(map(lambda x: (x, len(state['grid'])-1), locations)))

  return state

def populateDistanceGrid(startingLoc, state):
  distGrid = copy.deepcopy(state['distGrid']) # should be same size all -1
  distGrid[startingLoc[1]][startingLoc[0]] = 0 #set starting point in distance grid

  step = 0

  # do bfs
  while distGrid[state['endLoc'][1]][state['endLoc'][0]] == -1:
    boolMadeSteps = False
    for y in range(0, len(distGrid)):
      for x in range(0, len(distGrid[y])):
        if distGrid[y][x] == step:
          # test four directions to see if they are reachable and unset, 
          if x != 0 and distGrid[y][x-1] == -1 and state['grid'][y][x] + 1 >= state['grid'][y][x-1]:
            # not on the left edge and space to the left is unset and height to the left is <= 1 more than current height
            distGrid[y][x-1] = step + 1
            boolMadeSteps = True
          if x != len(distGrid[y]) -1 and distGrid[y][x+1] == -1 and state['grid'][y][x] + 1 >= state['grid'][y][x+1]:
            # not on the right edge and space to the left is unset and height to the left is <= 1 more than current height
            distGrid[y][x+1] = step + 1
            boolMadeSteps = True
          if y != 0 and distGrid[y-1][x] == -1 and state['grid'][y][x] + 1 >= state['grid'][y-1][x]:
            # not on the top edge and space up is unset and height up is <= 1 more than current height
            distGrid[y-1][x] = step + 1
            boolMadeSteps = True
          if y != len(distGrid) -1 and distGrid[y+1][x] == -1 and state['grid'][y][x] + 1 >= state['grid'][y+1][x]:
            # not on the bottom edge and space down is unset and height down is <= 1 more than current height
            distGrid[y+1][x] = step + 1
            boolMadeSteps = True
    step += 1
    if not boolMadeSteps:
      # we may not have found an answer but something is wrong
      print('Couldnt escape local minima')
      step = -1
      break
  return (distGrid, step)

def partOneSummary(state):
  (distGrid, step) = populateDistanceGrid(state['startLoc'], state)
  print(step)
  return step

def partTwoSummary(state):
  minStep = len(state['distGrid']) * len(state['distGrid'][0])
  for startingLoc in state['startingLocations']:
    (distGrid, step) = populateDistanceGrid(startingLoc, state)
    if step > 0 and step < minStep:
      minLoc = startingLoc
      minStep = step
      # print(distGrid)
      # print(minStep)
    if minStep < 24:
      print('we have a problem because you cant climb that fast')
      break
  print(minStep)
  return minStep
  
twelve = GenericProc('day12input.txt', state, lineLambda, partOneSummary, testInput, 31)
twelve.test()
print(twelve.run())

twelveTwo = GenericProc('day12input.txt', state, lineLambda, partTwoSummary, testInput, 29)
twelveTwo.test()
print(twelveTwo.run())

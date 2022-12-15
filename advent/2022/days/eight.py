from days.generic import GenericProc

testInput = '''30373
25512
65332
33549
35390'''

state = {
  'grid': []
}

def lineLambda(state, line):
  # we're just going to store the whole thing in state since we need the grid to do a calc. 

  state['grid'].append(list(line))
  return state

def lineVisibility(line):
  # returns an array of length equal to the line with False if a tree is not visible and True if it is 
  maxHeight = -1
  toReturn = []
  for tree in line:
    if int(tree) > maxHeight:
      maxHeight = int(tree)
      toReturn.append(1)
    else: 
      toReturn.append(0)
  return toReturn

def partOneSummary(state):
  visibilityMatrix = []
  # print(state['grid'])
  for row in state['grid']:
    #initialize vis matrix from left to right visibility
    visibilityMatrix.append(lineVisibility(row))

    backwards = row.copy()
    backwards.reverse()
    backBools = lineVisibility(backwards)
    backBools.reverse()
    # then do right to left
    for i in range(0, len(backBools)):
      visibilityMatrix[-1][i] = visibilityMatrix[-1][i] or backBools[i]

  # to keep directional logic by list instead of using grid itself rebuild as columns
  columns = [list(i) for i in zip(*state['grid'])]

  for col in range(0, len(columns)):

    # top down 
    visibilityCol = lineVisibility(columns[col])
    for j in range(0, len(visibilityCol)):
      visibilityMatrix[j][col] = visibilityMatrix[j][col] or visibilityCol[j]

    # and down to up
    columns[col].reverse()
    reverseVisibilityCol = lineVisibility(columns[col])
    for j in range(0, len(reverseVisibilityCol)):
      visibilityMatrix[len(visibilityMatrix)-1-j][col] = visibilityMatrix[len(visibilityMatrix)-1-j][col] or reverseVisibilityCol[j]
  
  total = sum([sum(x) for x in visibilityMatrix])

  return total

def score(val, view):
  toReturn = 0
  while toReturn < len(view) and view[toReturn] < val:
    toReturn += 1
  #include the tree you stopped on... 
  return toReturn +  (1 if toReturn < len(view) else 0)

def locScore(grid, columns, i, j):
  val = grid[i][j]
  left = grid[i][0:j]
  left.reverse()
  right = grid[i][j+1:]
  up = columns[j][0:i]
  up.reverse()
  down = columns[j][i+1:]

  return score(val, left) * score(val, up) * score(val, right)* score(val, down)\

def visScore(grid):
  columns = [list(i) for i in zip(*grid)]

  toReturn = [[0 for tree in row] for row in grid]

  for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
      toReturn[i][j] = locScore(grid, columns, i, j)

  return toReturn

def partTwoSummary(state):
  visibilityScore = visScore(state['grid'])
  print(max([ max(row) ] for row in visibilityScore)) # why is this outter max returning an list, don't care
  return max([ max(row) ] for row in visibilityScore)[0]

eight = GenericProc('day8input.txt', state, lineLambda, partOneSummary, testInput, 21)
eight.test()
eight.run()

eightTwo = GenericProc('day8input.txt', state, lineLambda, partTwoSummary, testInput, 8)
eightTwo.test()
eightTwo.run()
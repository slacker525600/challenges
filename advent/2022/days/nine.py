from days.generic import GenericProc

testInput = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

largerTest = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

class Point():

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def updateLoc(self, xDif, yDif):
    self.x = self.x + xDif
    self.y = self.y + yDif

  def moveTail(self, head):
    xDif = head.x - self.x
    yDif = head.y - self.y
    # determine if move is needed and what it is then apply the change to coordinates
    if abs(xDif) > 1 or abs(yDif) > 1: 
      if (xDif != 0 and yDif != 0):
        # diagonal move, 
        self.x = self.x + int(xDif/abs(xDif))
        self.y = self.y + int(yDif/abs(yDif))
      elif abs(xDif) == 2:
        self.x = self.x + 1 * (1 if xDif > 0 else -1)
      elif abs(yDif) == 2:
        self.y = self.y + 1 * (1 if yDif > 0 else -1)
      else:
        print('Huge mistake?')
    return self.pos()

  def pos(self):
    return (self.x, self.y)

  def __str__(self) -> str:
    return f'{self.x} {self.y}'

state = {
  'visitedGridTail1': [(0,0)],
  'visitedGridTail10': [(0,0)],
  'ropePoints': [Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(0,0)]
}


# basically have a grid, and a dot moving in it, current location, 
# grid starts as single cell, grows when boundaries hit, 
# B means both head and tail, H/T for head/tail, # for visited, . for not, 

def lineLambda(state, line):
  # each instruction is multiple moves, move head, determine where tail is, update visited list and current positions

  direction = line[0]
  steps = int(line[2:])
  (x,y) = (0 if direction in ('U', 'D') else 1 if direction == 'R' else -1, 
           0 if direction in ('L', 'R') else 1 if direction == 'U' else -1)
  
  for step in range(0,steps):
    state['ropePoints'][0].updateLoc(x, y)
    #print(f'moved head to {state["ropePoints"][0].pos()}')
    # tail doesn't move for every head move as overlaps, and diagonals are acceptable. 
    for knotIndex in range(1,len(state['ropePoints'])):
      state['ropePoints'][knotIndex].moveTail(state['ropePoints'][knotIndex - 1])      
      #print(f'updating knot {knotIndex} to {state["ropePoints"][knotIndex].pos()}' )
    if state['ropePoints'][1].pos() not in state['visitedGridTail1']:
      state['visitedGridTail1'].append(state['ropePoints'][1].pos())
    if state['ropePoints'][-1].pos() not in state['visitedGridTail10']:
      state['visitedGridTail10'].append(state['ropePoints'][-1].pos())
  return state

def partOneSummary(state):
  return len(state['visitedGridTail1'])

def partTwoSummary(state):
  return len(state['visitedGridTail10'])

nine = GenericProc('days/day9input.txt', state, lineLambda, partOneSummary, testInput, 13)
nine.test()
print(nine.run())

nineTwo = GenericProc('days/day9input.txt', state, lineLambda, partTwoSummary, testInput, 1)
nineTwo.test()
nineTwoLarge = GenericProc('days/day9input.txt', state, lineLambda, partTwoSummary, largerTest, 36)
nineTwoLarge.test()
print(nineTwo.run())


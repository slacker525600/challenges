# just opening a file for starting...

def run():
  print("Hello world!")
  # one()
  # oneGeneric()
  two()

def one():
  f = open('day1input.txt','r')
  s = f.readline()
  elfVal = 0
  elfTotals = []
  while s:
    if len(s.strip())>0:
      elfVal = elfVal + int(s)
    else:
      elfTotals.append(elfVal)
      elfVal = 0
    s = f.readline()
  elfTotals.sort()

  print(sum(elfTotals[-1:]))
  print(sum(elfTotals[-3:]))

def oneGeneric():
  stateObject = { 
    'elfTotals': [],
    'elfVal': 0 
  }
  def lineLambda(state, line):
    if(len(line) > 0):
      state['elfVal'] = state['elfVal'] + int(line)
    else:
      state['elfTotals'].append(state['elfVal'])
      state['elfVal'] = 0
    return state

  def summaryLambda(state):
    state['elfTotals'].sort()
    print(sum(state['elfTotals'][-1:]))
    print(sum(state['elfTotals'][-3:]))


  generic('day1input.txt', stateObject, lineLambda, summaryLambda )

def generic(inputFile, state, lineLambda, summaryLambda):
  f = open(inputFile,'r')
  s = f.readline()
  while s:
    line = s.strip()
    state = lineLambda(state, line)
    s = f.readline()
  summaryLambda(state)


def two():
  scoreDict = {'R':1, 'P':2, 'S':3}

  def partOnelineLambda(state, line):
    lineScore = 0
    [opponent, me] = line.split()

    rpsOp = 'R' if opponent == 'A' else ('P' if (opponent == 'B') else 'S')
    rpsMe = 'R' if me == 'X' else ('P' if (me == 'Y') else 'S')

    if rpsOp == rpsMe:
      lineScore += 3
    elif (rpsOp == 'R' and rpsMe == 'P') or (rpsOp == 'P' and rpsMe == 'S') or (rpsOp == 'S' and rpsMe == 'R'):
      lineScore += 6

    lineScore += scoreDict[rpsMe]

    print(line, rpsOp, rpsMe, lineScore, state)

    state['score'] = state['score'] + lineScore
    return state

  def partTwolineLambda(state, line):
    lineScore = 0
    [opponent, me] = line.split()
    # weird way to think about it, but rock beats scissors, scissors beat paper, paper beats rock, 
    # so in an array index of + offset of -1 0 1 gives you your throw 
    offsets = ['P','S','R']
    
    rpsOp = 'R' if opponent == 'A' else ('P' if (opponent == 'B') else 'S')
    resultOffset = -1 if me == 'X' else (0 if (me == 'Y') else 1)
    print(offsets.index(rpsOp), resultOffset, offsets[(offsets.index(rpsOp)+resultOffset) %3])
    rpsMe = offsets[(offsets.index(rpsOp)+resultOffset) %3]

    if rpsOp == rpsMe:
      lineScore += 3
    elif (rpsOp == 'R' and rpsMe == 'P') or (rpsOp == 'P' and rpsMe == 'S') or (rpsOp == 'S' and rpsMe == 'R'):
      lineScore += 6
    if lineScore != resultOffset*3 + 3:
      print('Bug?')

    lineScore += scoreDict[rpsMe]

    print(line, rpsOp, rpsMe, lineScore, state)

    state['score'] = state['score'] + lineScore
    return state

  def summaryLambda(state):
    print(state)

  stateObject = {'score': 0}
  generic('day2input.txt', stateObject, partOnelineLambda, summaryLambda )

  stateObject = {'score': 0}
  generic('day2input.txt', stateObject, partTwolineLambda, summaryLambda )


# read input, track state, perform actions with line (update state)



if __name__ == "__main__":
  run()
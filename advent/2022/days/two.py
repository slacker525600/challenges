from generic import generic
from io import StringIO

def two():
  throwScoreDict = {'R':1, 'P':2, 'S':3}
  matchScoreDict = {
    'R': { 'R':3, 'P':6, 'S':0 }, 
    'P': { 'R':0, 'P':3, 'S':6 }, 
    'S': { 'R':6, 'P':0, 'S':3 }
  }
  defaultState = {'score': 0}


  def partOnelineLambda(state, line):
    lineScore = 0
    [opponent, me] = line.split()

    rpsOp = 'R' if opponent == 'A' else ('P' if (opponent == 'B') else 'S')
    rpsMe = 'R' if me == 'X' else ('P' if (me == 'Y') else 'S')

    lineScore += matchScoreDict[rpsOp][rpsMe]
    lineScore += throwScoreDict[rpsMe]

    # print(line, rpsOp, rpsMe, lineScore, state)

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
    # print(offsets.index(rpsOp), resultOffset, offsets[(offsets.index(rpsOp)+resultOffset) %3])
    rpsMe = offsets[(offsets.index(rpsOp)+resultOffset) %3]

    lineScore += matchScoreDict[rpsOp][rpsMe]
    if matchScoreDict[rpsOp][rpsMe] != resultOffset*3 + 3:
      print('Bug?')

    lineScore += throwScoreDict[rpsMe]

    # print(line, rpsOp, rpsMe, lineScore, state)

    state['score'] = state['score'] + lineScore
    return state

  def summaryLambda(state):
    print(state['score'])
    return state['score']

  test = StringIO('''A Y
B X
C Z''')

  assert generic(test,defaultState, partOnelineLambda, summaryLambda) == 15

  with open('day2input.txt','r') as f:
    generic(f, defaultState, partOnelineLambda, summaryLambda )

  test = StringIO('''A Y
B X
C Z''')

  assert generic(test,defaultState, partTwolineLambda, summaryLambda) == 12

  with open('day2input.txt','r') as f:
    generic(f, defaultState, partTwolineLambda, summaryLambda )

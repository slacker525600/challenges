from generic import generic

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


# just opening a file for starting...

def run():
  print("Hello world!")
  one()
  oneGeneric()
  #two()

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
  stateObject = {}
  def lineLambda(state, line):
    return state
  def summaryLambda(state):
    print(state)
  generic('day2input.txt', stateObject, lineLambda, summaryLambda )


# read input, track state, perform actions with line (update state)



if __name__ == "__main__":
  run()
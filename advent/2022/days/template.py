from days.generic import GenericProc

testInput = ''''''

state = {
}

def lineLambda(state, line):
  return state

def partOneSummary(state):
  return -1

def partTwoSummary(state):
  return -1
  
nine = GenericProc('daynineinput.txt', state, lineLambda, partOneSummary, testInput, 95437)
nine.test()
print(nine.run())

nineTwo = GenericProc('day9input.txt', state, lineLambda, partTwoSummary, testInput, 24933642)
nineTwo.test()
print(nineTwo.run())


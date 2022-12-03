from days.generic import generic, GenericProc
from io import StringIO
from functools import reduce

inputFileName = 'days/day3input.txt'
defaultState = {
  'items': [],
  'group': [],
  'groupSum':0
}

def priorityVal(char):
  val = ord(char) - ord('a') + 1
  val = val if val > 0 else val + ord('a') - ord('A') + 26
  return val

def lineLambda(state, line):
  # create two sets from first and second half of a line
  intersect = set(line[:(int(len(line)/2))]).intersection(set(line[(int(len(line)/2)):]))
  state['items'].append(list(intersect)[0])
  state['group'].append(line)

  if len(state['group']) == 3:
    intersectChar = list(set(state['group'][0]).intersection(set(state['group'][1])).intersection(set(state['group'][2])))
    print('intersectChar', intersectChar)
    if(len(intersectChar) >1):
      print('BUG')
    else:
      state['groupSum'] += priorityVal(intersectChar[0])
      state['group'] = []
  return state

def summaryLambdaOne(state):
  priorityVals = list(map( priorityVal, state['items']))
  print(sum(priorityVals))
  #part 1 return sum(priorityVals)
  return sum(priorityVals)

def summaryLambdaTwo(state):
  print(state['groupSum'])
  return state['groupSum']

testString = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

three = GenericProc(inputFileName, defaultState, lineLambda, summaryLambdaOne, testString, testSolution = 157)

three.test()
print('but why', defaultState)
print(three.run())

threePartTwo = GenericProc(inputFileName, defaultState, lineLambda, summaryLambdaTwo, testString, testSolution= 70)

threePartTwo.test()
print(threePartTwo.run())

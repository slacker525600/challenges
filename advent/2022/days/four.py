from days.generic import GenericProc

inputFileName = 'day4input.txt'

testInput = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

state = {
  'containCount': 0,
  'overlapCount': 0
}

def lineToRanges(line):
  a, b = line.split(',')
  aMin, aMax = a.split('-')
  bMin, bMax = b.split('-')
  return (int(aMin),int(aMax)),(int(bMin),int(bMax))

def rangeContains(a, b):
  return a[0] <= b[0] and a[1] >= b[1]

def rangeOverlaps(a, b):
  # just putting a quick try to avoid edge case bs if any range boundary = they overlap
  if a[0] == b[0] or a[1] == b[1] or a[1] == b[0] or a[0] == b[1]:
    return True
  elif (a[0] < b[0] and a[1] > b[0]) or (b[0] < a[0] and b[1] > a[0]):
    # if A's min is less than Bs and As max goes past Bs min or vice versa
    return True
  return False

def lineLambdaPartOne(state, line):
  a, b = lineToRanges(line)
  if rangeContains(a, b) or rangeContains(b, a):
    state['containCount'] += 1
  if rangeOverlaps(a, b):
    state['overlapCount'] += 1
  return state

def partOneSummary(state):
  print(state)
  return state['containCount']

def partTwoSummary(state):
  print(state)
  return state['overlapCount']

four = GenericProc(inputFileName, state, lineLambdaPartOne, partOneSummary, testInput, 2)
four.test()
four.run()

fourTwo = GenericProc(inputFileName, state, lineLambdaPartOne, partTwoSummary, testInput, 4)
fourTwo.test()
fourTwo.run()

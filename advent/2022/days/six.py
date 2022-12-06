from days.generic import GenericProc

testInput = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

state = {
  'charAt': 0,
  'signal': [None,None,None,None],
  'signalTwo': [None,None,None,None,None,None,None,None,None,None,None,None,None,None],
  'endFound': 0,
  'startFound': 0
}

def lineLambdaPartOne(state, char):
  if(state['endFound'] > 0 and state['startFound'] > 0):
    return state
  print(state, char)
  state['charAt'] += 1

  state['signal'][state['charAt'] % 4] = char
  state['signalTwo'][state['charAt'] % 14] = char

  if state['endFound'] == 0 and state['signal'][0] is not None and  state['signal'][1] is not None and \
   state['signal'][2] is not None and  state['signal'][3] is not None and \
     len(set(state['signal'])) == 4:
     state['endFound'] = state['charAt']
  if len(set(state['signalTwo'])) == 14 and None not in state['signalTwo']:
    state['startFound'] = state['charAt']
  return state

def partOneSummary(state):
  print(state, state['endFound'])
  return state['endFound']
def partTwoSummary(state):
  print(state, state['startFound'])
  return state['startFound']



six = GenericProc('days/day6input.txt', state, lineLambdaPartOne, partOneSummary, testInput, 7, byChar = True)
six.test()
six.run()

sixTwo = GenericProc('days/day6input.txt', state, lineLambdaPartOne, partTwoSummary, testInput, 19, byChar = True)
sixTwo.test()
sixTwo.run()

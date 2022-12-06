from days.generic import GenericProc

# really need queues, could push and reverse if efficiency is an issue but meh
state = {
  'mode': 'prep',
  'queuedStacks': [],
  'stacks': []
}

def lineProc(state, line):
  if (state['mode'] == 'prep'):
    # load up stacks
    state['queuedStacks'].append(line)
    if not len(line):
      # create stacks from lines
      # create a list/stack for each column
      state['stacks'] = [ [] for x in state['queuedStacks'][-2].split() ]
      state['partTwoStacks'] = [ [] for x in state['queuedStacks'][-2].split() ]

      stacks = state['queuedStacks'][:-2]
      stacks.reverse()
      for row in stacks:
        # for each item here push into list with index blah 
        # manually edited input to have # in the front -> letters to different location, 
        # allows fudging generic logic with spaces up front 
        i = 0
        while i*4 < len(row):
          if(row[i*4+2] != ' '):
            state['stacks'][i].append(row[i*4+2])
            state['partTwoStacks'][i].append(row[i*4+2])
          i += 1

      state['queuedStacks'] = []
      state['mode'] = 'moving',
  else: 
    move = line.split()
    # move num from num to num
    count = int(move[1])
    giver = int(move[3])
    taker = int(move[5])
    i = 0
    while i < count:
      state['stacks'][taker-1].append(state['stacks'][giver-1].pop())
      i += 1

    # partTwoStacks
    state['partTwoStacks'][taker-1].extend(state['partTwoStacks'][giver-1][(0-count):])
    state['partTwoStacks'][giver-1] = state['partTwoStacks'][giver-1][:(0-count)]
  return state

def summaryLambda(state):
  result = ''.join(map(lambda x: x[-1], state['stacks']))
  return result

def summaryLambdaPartTwo(state):
  result = ''.join(map(lambda x: x[-1], state['partTwoStacks']))
  return result


sampleInput = '''#    [D]    
#[N] [C]    
#[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


five = GenericProc('days/day5input.txt', state, lineProc, summaryLambda, sampleInput, 'CMZ')
five.test()
print(five.run())

five = GenericProc('days/day5input.txt', state, lineProc, summaryLambdaPartTwo, sampleInput, 'MCD')
five.test()
print(five.run())
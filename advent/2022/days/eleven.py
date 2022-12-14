from days.generic import GenericProc

testInput = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
Starting items: 74
Operation: new = old + 3
Test: divisible by 17
If true: throw to monkey 0
If false: throw to monkey 1'''

state = {
  'chunk': [],
  'monkeys': []
}

def splitChunk(chunk):
  # print(chunk)
  label = int(chunk[0][7:-1] ) # monkey label, believe these are in order 
  startingItems = list(map(int, chunk[1][16:].split(',')))
  modificationRule = chunk[2][17:]
  divisibilityTest = int(chunk[3][19:]) # this assumes all tests are divisibility
  trueDest = int(chunk[4][25:])
  falseDest = int(chunk[5][26:])
  return (label, startingItems, modificationRule, divisibilityTest, trueDest, falseDest)

class Monkey():
  def __init__(self, chunk):
    (label, startingItems, modificationRule, divisibilityTest, trueDest, falseDest) = splitChunk(chunk)
    self.label = label
    self.startingItems = startingItems
    self.modificationRule = modificationRule
    self.divisibilityTest = divisibilityTest
    self.trueDest = trueDest
    self.falseDest = falseDest
    self.inspectCount = 0

  def __repr__(self) -> str:
    return f'{self.label}, {self.startingItems}, {self.modificationRule}, {self.divisibilityTest}, {self.trueDest}, {self.falseDest}'
  
  def addItem(self, item):
    self.startingItems.append(item)

  def act(self, maxModulo):
    # takes first item off list, inspects it, applying the modifier, divides by three and rounds, then throws to new monkey based on test
    old = self.startingItems[0]
    self.startingItems = self.startingItems[1:]
    # modification Rule has old in an fstring 
    newVal = eval(self.modificationRule)
    # newVal = int(newVal/3)
    self.inspectCount += 1
    dest = self.trueDest if newVal % self.divisibilityTest == 0 else self.falseDest
    # print('val, test, true,false, decided',  newVal, self.divisibilityTest, self.trueDest, self.falseDest, dest)
    newVal = newVal % maxModulo
    return (dest, newVal)

def lineLambda(state, line):
  if not line:
    state['monkeys'].append(Monkey(state['chunk']))
    state['chunk'] = []
  else:
    state['chunk'].append(line)
  return state

def partOneSummary(state):
  # didn't add the last monkey yet
  state['monkeys'].append(Monkey(state['chunk']))

  for round in range(0,20):
    for monkeyIndex in range(0, len(state['monkeys'])):
      monkey = state['monkeys'][monkeyIndex]
      # really just need to do the actions for all the items
      while monkey.startingItems:
        (dest, val) = monkey.act()
        #  print('dest, val', dest, val)
        state['monkeys'][dest].addItem(val)
    # break

  state['monkeys'].sort(reverse=True, key=lambda x: x.inspectCount)
  print(state['monkeys'][0].inspectCount, state['monkeys'][1].inspectCount)
  return state['monkeys'][0].inspectCount * state['monkeys'][1].inspectCount

def partTwoSummary(state):
  # didn't add the last monkey yet
  state['monkeys'].append(Monkey(state['chunk']))

  maxModulo = 1
  for monkey in state['monkeys']:
    maxModulo *= monkey.divisibilityTest
  for round in range(0,10000):
    for monkeyIndex in range(0, len(state['monkeys'])):
      monkey = state['monkeys'][monkeyIndex]
      # really just need to do the actions for all the items
      while monkey.startingItems:
        (dest, val) = monkey.act(maxModulo)
        #  print('dest, val', dest, val)
        state['monkeys'][dest].addItem(val)
    # break

  state['monkeys'].sort(reverse=True, key=lambda x: x.inspectCount)
  print(state['monkeys'][0].inspectCount, state['monkeys'][1].inspectCount)
  return state['monkeys'][0].inspectCount * state['monkeys'][1].inspectCount
  
# eleven = GenericProc('days/day11input.txt', state, lineLambda, partOneSummary, testInput, 10605)
# eleven.test()
# print(eleven.run())

elevenTwo = GenericProc('days/day11input.txt', state, lineLambda, partTwoSummary, testInput, 2713310158)
elevenTwo.test()
print(elevenTwo.run())



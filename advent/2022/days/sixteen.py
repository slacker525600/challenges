from days.generic import GenericProc

testInput = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

state = {
  'valves': {},
  'labelsByFlow': []
}

class Valve():
  def __init__(self, label, flow, leadsTo):
    self.label = label
    self.flow = flow
    self.leadsTo = leadsTo
    self.indirect = { label:0 }
    for label in leadsTo:
      self.indirect[label] = 1

  def __repr__(self):
    # char10 newline? 
    return f'{self.label}:{self.flow} -> {",".join(self.leadsTo)}'

  def setDistances(self, state):
    distance = 1
    lastLoop = self.leadsTo
    while len(self.indirect) < len(state['valves']):
      # we've already added lastLoop at distance, check all those things for labels we don't have 
      distance += 1
      thisLoop = []
      for label in lastLoop:
        for connection in state['valves'][label].leadsTo:
          if self.indirect.get(connection):
            continue
          else:
            thisLoop.append(connection)
            self.indirect[connection] = distance
      lastLoop = thisLoop
      # print(self.indirect)
      
  def getDistance(self, label):
    return self.indirect[label]

def parseLine(line):
  newLine = line.replace('Valve ', ''). \
      replace(' has flow rate=', '|'). \
      replace('; tunnels lead to valves ', '|'). \
      replace('; tunnel leads to valve ', '|')
  relevant = newLine.split('|')

  return Valve(relevant[0], int(relevant[1]), relevant[2].split(', '))

def lineLambda(state, line):
  # print(line)
  valve = parseLine(line)
  print(valve)
  state['valves'][valve.label] = valve
  return state

def currentFlow(state, openValves):
  flow = 0
  for label in openValves:
    flow += state['valves'][label].flow
  return flow

def heuristicRank(label, remainingSteps, state, currentLocation, labelsRemaining):
  # add weight of output from this label, and proximity to other high volume labels, 
  value = (remainingSteps - state['valves'][currentLocation].getDistance(label)) * state['valves'][label].flow
  # 
  value -= sum([state['valves'][label].getDistance(others) * state['valves'][others].flow for others in labelsRemaining])
  return value

def identifyNextStep(state, currentLocation, openValves, remainingSteps):
  nextIndex = 0
  if len(openValves) == len(state['labelsByFlow']):
    return None, None
  labelsRemaining = [label for label in state['labelsByFlow'] if label not in openValves and state['valves'][currentLocation].getDistance(label)<remainingSteps]
  state['labelsByFlow'].sort(key= lambda x: heuristicRank(x, remainingSteps, state, currentLocation, labelsRemaining), reverse=True)
  #for label in [valve for valve in state['labelsByFlow'] if label not in openValves]:
  
  nextLabel = labelsRemaining[0]

  state['valves'][currentLocation].getDistance(nextLabel)
  if currentLocation != 'AA':
    nextIndex = state['labelsByFlow'].index(currentLocation) + 1
  nextLabel = state['labelsByFlow'][nextIndex]
  return state['valves'][currentLocation].getDistance(nextLabel), nextLabel


def partOneSummary(state):
  for valve in state['valves'].values():
    # print(valve)
    if valve.flow:
      state['labelsByFlow'].append(valve.label)
    valve.setDistances(state)
  state['labelsByFlow'].sort(key=lambda x: state['valves'][x].flow, reverse=True)
  print(state['labelsByFlow'])
  # ['AA'].printAll(state)
  # how are we going to find the max, starting at AA find path to each valve 
  # sort valves by flow rate, 
  maxFlow = 0 
  steps = 0
  openValves = []
  label = 'AA'
  while steps < 30:
    print('moving from', label, 'current total', maxFlow, 'Current Flow', currentFlow(state, openValves))
    distance, label = identifyNextStep(state, label, openValves, 30 - steps)
    if distance is None:
      break
    # attempt to reach and turn valve, cost is distance and activation 1
    stepsTaken = distance+1
    maxFlow += currentFlow(state, openValves)*stepsTaken
    print('to ', label, 'away', distance, 'steps remaining', 30 - steps, 'new total', maxFlow)
    openValves.append(label)
    steps += stepsTaken
  maxFlow += currentFlow(state, openValves)*(30 - steps)
  print('Max Flow', maxFlow)
  return maxFlow

def partTwoSummary(state):
  return -1
  
nine = GenericProc('daynineinput.txt', state, lineLambda, partOneSummary, testInput, 1651)
nine.test()
print(nine.run())

nineTwo = GenericProc('day9input.txt', state, lineLambda, partTwoSummary, testInput, 24933642)
nineTwo.test()
print(nineTwo.run())


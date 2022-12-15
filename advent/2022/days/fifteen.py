from days.generic import GenericProc

testInput = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

state = {
  'pairs': []
}

class Pair():
  def __init__(self, sensorX, sensorY, beaconX, beaconY):
    self.sensorX = sensorX
    self.sensorY = sensorY
    self.beaconX = beaconX
    self.beaconY = beaconY
  def rowRange(self, row):
    # given a row number, determine the range of coordinates excluded from this observation
    # taxicab distance of beacon and sensor, perpendicular distance to row, and then apply leftovers in both direction
    distance = abs(self.sensorX - self.beaconX ) + abs(self.sensorY - self.beaconY)
    if not (self.sensorY - distance <= row and row <= self.sensorY + distance):
      #print('no overlap', self, ' row ', row)
      return None
    else:
      return self.sensorX - (distance - abs(self.sensorY - row)), self.sensorX + (distance - abs(self.sensorY - row))
    
  def __repr__(self):
    return f'[({self.sensorX} {self.sensorY}), ({self.beaconX} {self.beaconY})]'

# for each pair beacon sensor we have a coordinate, 
# given a line number, starting at ? determine how many locations are not possible beacon locations. 
# for each pair, range at that row, remove overlaps, sum of the ranges, 

def lineLambda(state, line):
  # Sensor at x=20, y=1: closest beacon is at x=15, y=3')
  # Sensor at |20|1| closest beacon is at |15|3')
  line = line.replace('x=', '|').replace(':', '|').replace(', y=', '|') 
  lineSegments = line.split('|') # (throwaway) (first coords throwaway) (second coords )
  state['pairs'].append(Pair(int(lineSegments[1]), int(lineSegments[2]), int(lineSegments[-2]), int(lineSegments[-1])))

  return state

def partOneSummary(state):
  cantBe = set()
  beaconsOnRow = set()
  for pair in state['pairs']:
    pairRange = pair.rowRange(10)
    if pairRange:
      #print(pairRange)
      cantBe = cantBe.union(range(pairRange[0], pairRange[1] +1))
      if(pair.beaconY == 10):
        beaconsOnRow.add(pair.beaconX)
  print(len(cantBe) , len(beaconsOnRow))
  
  cantBe = set()
  beaconsOnRow = set()
  for pair in state['pairs']:
    pairRange = pair.rowRange(2000000)
    if pairRange:
      #print(pairRange)
      cantBe = cantBe.union(range(pairRange[0], pairRange[1] +1))
      if(pair.beaconY == 2000000):
        beaconsOnRow.add(pair.beaconX)
  print(len(cantBe) , len(beaconsOnRow))
  cantBe.difference(beaconsOnRow)
  return 26

# copied from day 4
def rangeOverlaps(a, b):
  # just putting a quick try to avoid edge case bs if any range boundary = they overlap
  if a[0] == b[0] or a[1] == b[1] or a[1] == b[0] or a[0] == b[1]:
    return True
  elif (a[0] < b[0] and a[1] > b[0]) or (b[0] < a[0] and b[1] > a[0]):
    # if A's min is less than Bs and As max goes past Bs min or vice versa
    return True
  return False

def mergeRanges(aRanges, b, firstOverlap):
  # array of ranges that are excluded, merge in new range b 
  aRanges[firstOverlap] = (min(aRanges[firstOverlap][0], b[0]), max(aRanges[firstOverlap][1], b[1]))
  while firstOverlap < len(aRanges) - 1:
    # do we need to merge the next range into this range, 
    # update max at first overlap, and remove next entry, 
    # if not, break and return full array
    if aRanges[firstOverlap+1][0] <= aRanges[firstOverlap][1] + 1:
       aRanges[firstOverlap] = (aRanges[firstOverlap][0], max(aRanges.pop(firstOverlap+1)[1], aRanges[firstOverlap][1]))
    else:
      break
  return aRanges

def partTwoSummary(state):
  print('Part 2')
  beaconsOnRow = set()
  for row in range(0, 4000000):
    cantBe = [] # array of ranges returned from pairs, should be merged /appended bubbly
    for pair in state['pairs']:
      pairRange = pair.rowRange(row)
      # print(row, pairRange)
      if pairRange:
        if not cantBe:
          cantBe.append(pairRange)
        else:
          # merge this range into the array, 
          # range from this set at this row, 
          # print('pre merge', cantBe, pairRange, pair)
          rangeIndex = 0
          mergedRange = False
          while rangeIndex < len(cantBe):
            eachRange = cantBe[rangeIndex]
            if rangeOverlaps(pairRange, eachRange):
              cantBe = mergeRanges(cantBe, pairRange, rangeIndex)
              break
            elif pairRange[1] < eachRange[0]:
              cantBe.insert(rangeIndex, pairRange)
              break                          
            rangeIndex += 1
          if cantBe[-1][1] < pairRange[1]:
            cantBe.append(pairRange)
          # print('post merge', cantBe)
    if len(cantBe) > 1:
      print(row, cantBe)
    elif cantBe[0][0] >0 or cantBe[0][1] < 4000000:
      print(row, cantBe)
  
  return -1
  
fifteen = GenericProc('day15input.txt', state, lineLambda, partOneSummary, testInput, 26)
fifteen.test()
print(fifteen.run())

fifteenTwo = GenericProc('day15input.txt', state, lineLambda, partTwoSummary, testInput, -1)
#print('test 2 ')
#fifteenTwo.test()
print('test 2 finished')
print(fifteenTwo.run())


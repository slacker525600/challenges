from days.generic import GenericProc

testInput = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

state = {
  'cycle': 1,
  'register': 1,
  'acc': 0,
  'lineArray': [],
  'lineAcc': ''
}

def pixel(cycle):
  return (cycle - 1) % 40

def lineLambda(state, line):
  # line is operation, 
  # increase cycle count and update register 
  # if cycle count in the middle of executing was 20 % 40 == 0 acc += cycle * register 
  # print(state, line)
  # always render the pixel of the cycle
  state['lineAcc'] += '.' if abs(pixel(state['cycle']) - state['register']) > 1 else '#'
  inc = 0
  if line[0:4] == 'noop':
    inc = 1
  if line[0:4] == 'addx':
    inc = 2

  # cheating here a bit, since cycle count only increases by 1 or 2, next inc will be = if 2 so only need off by one I think
  if state['cycle'] % 40 == 20:
    state['acc'] += state['cycle'] * state['register']
  elif inc == 2 and state['cycle'] % 40 < 20 and (state['cycle'] + 1) % 40 == 20:
    state['acc'] += (state['cycle'] + 1) * state['register']

  if inc == 2:
    # sometimes render the pixel before the next operation completes
    state['lineAcc'] += '.' if abs(pixel(state['cycle'] + 1) - state['register']) > 1 else '#'
    # add op 
    state['register'] += int(line[5:])
  state['cycle'] += inc

  if len(state['lineAcc']) >= 40:
    state['lineArray'].append(state['lineAcc'][:40])
    state['lineAcc'] = state['lineAcc'][40:]

  return state

def partOneSummary(state):
  print(state['acc'])
  return state['acc']

def partTwoSummary(state):
  for line in state['lineArray']:
    print(line)
  return '\n'.join(state['lineArray'])
  
ten = GenericProc('days/day10input.txt', state, lineLambda, partOneSummary, testInput, 13140)
ten.test()
print(ten.run())

testTwoOut = '''##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....'''

tenTwo = GenericProc('days/day10input.txt', state, lineLambda, partTwoSummary, testInput, testTwoOut)
tenTwo.test()
print(tenTwo.run())

argh = '''
####...##..##..####.###...##..#....#..#.
#.......#.#..#.#....#..#.#..#.#....#..#.
###.....#.#....###..#..#.#....#....####.
#.......#.#....#....###..#.##.#....#..#.
#....#..#.#..#.#....#....#..#.#....#..#.
####..##...##..#....#.....###.####.#..#.
'''
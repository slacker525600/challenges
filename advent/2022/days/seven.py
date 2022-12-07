from days.generic import GenericProc

testInput = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

state = {
  'command': None,
  'pwd': '/',
  'folders': {},
  'directoryNames': [],
  'files': []
}

class folder():
  directoryNames = []
  files = []
  size = None

  def __init__(self, directoryNames, files):
    self.directoryNames = directoryNames
    self.files = files
  def __str__(self):
    return str(self.directoryNames) + str(self.files)
  def calcSize(self, state):
    if self.size is None:
      self.size = sum(self.files)
      for directory in self.directoryNames:
        self.size += state['folders'][directory].calcSize(state)

    return self.size

def addLs(state):
  state['folders'][state['pwd']] = folder(state['directoryNames'], state['files'])
  state['directoryNames'] = []
  state['files'] = []


def lineLambda(state, line):
  # print(state, line)
  if line[0] == '$':
    # new command, so finish proc of last, and update state
    if state['command'] is not None and state['command'][:4] == '$ ls':
      addLs(state)
    # processed state from last
    state['command'] = line
    if line[:4] == '$ cd':
      dir = line.split()[-1]
      if (dir == '..'):
        state['pwd'] = state['pwd'][:(state['pwd'][:-1].rindex('/')+1)]
      elif (dir == '/'):
        state['pwd'] = '/'
      else:
        state['pwd'] += dir + '/'
  else:
    #only other thing in current output is directories and file sizes
    if line[:3] == 'dir':
      state['directoryNames'].append(state['pwd'] + line[4:] + '/')
    else:
      state['files'].append(int(line.split()[0]))
  # is this a new command or output from a prior
  return state

def partOneSummary(state):
  if (len(state['directoryNames']) or len(state['files'])):
    addLs(state)

  toReturn = 0
  for key, folder in state['folders'].items():
    # key is folderPath
    size = folder.calcSize(state)
    if (size <= 100000):
      toReturn += size
  return toReturn

def partTwoSummary(state):
  if (len(state['directoryNames']) or len(state['files'])):
    addLs(state)

  toReturn = 0
  for key, folder in state['folders'].items():
    # key is folderPath
    size = folder.calcSize(state)
    if (size <= 100000):
      toReturn += size

  total = 70000000
  remaining = total - state['folders']['/'].calcSize(state)
  updateSize = 30000000
  need = updateSize - remaining

  possibilities = list(filter(lambda folder: folder.calcSize(state) >= need, state['folders'].values()))
  minAvailableSize = min(map(lambda folder: folder.calcSize(state), possibilities))
  print(minAvailableSize)

  return minAvailableSize


seven = GenericProc('days/day7input.txt', state, lineLambda, partOneSummary, testInput, 95437)
seven.test()
seven.run()

sevenTwo = GenericProc('days/day7input.txt', state, lineLambda, partTwoSummary, testInput, 24933642)
sevenTwo.test()
sevenTwo.run()

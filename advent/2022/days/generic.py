import io
import copy
# generic solution to processing a file line by line
def generic(inputFile, defaultState, lineLambda, summaryLambda):
  """ read input, 
      track state, 
      perform actions with lines of input (update state)
  """
  state = defaultState.copy()
  s = inputFile.readline()
  while s:
    line = s.strip()
    state = lineLambda(state, line)
    s = inputFile.readline()
  return summaryLambda(state)

class GenericProc():
  inputFileName = ''
  defaultState = {}
  lineLambda = lambda x: x 
  summaryLambda  = lambda x: x 
  testString = ''
  testSolution = ''
  byChar = False

  def __init__(self, inputFileName, defaultState, lineLambda, summaryLambda, testString, testSolution, byChar = False):
    self.inputFileName = inputFileName
    self.defaultState = defaultState
    self.lineLambda = lineLambda
    self.summaryLambda  = summaryLambda
    self.testString = testString
    self.testSolution = testSolution
    self.byChar = byChar

  def test(self):
    assert self.summaryLambda(self.fileRun(io.StringIO(self.testString))) == self.testSolution

  def fileRun(self, f):
    state = copy.deepcopy(self.defaultState)
    if (self.byChar):
      s = f.read(1)
    else:
      s = f.readline()
    while s:
      line = s.strip()
      state = self.lineLambda(state, line)
      if (self.byChar):
        s = f.read(1)
      else:
        s = f.readline()
    return state

  def run(self):
    with open(self.inputFileName,'r') as f:
      state = self.fileRun(f)
      return self.summaryLambda(state)    

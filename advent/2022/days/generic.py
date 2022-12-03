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

  def __init__(self, inputFileName, defaultState, lineLambda, summaryLambda, testString, testSolution):
    print('initializing')
    self.inputFileName = inputFileName
    self.defaultState = defaultState
    self.lineLambda = lineLambda
    self.summaryLambda  = summaryLambda
    self.testString = testString
    self.testSolution = testSolution

  def test(self):
    state = copy.deepcopy(self.defaultState)
    assert generic(io.StringIO(self.testString), state, self.lineLambda, self.summaryLambda) == self.testSolution
    print('after test', self.defaultState)


  def run(self):
    with open(self.inputFileName,'r') as f:
      print(self.defaultState)
      state = copy.deepcopy(self.defaultState)
      s = f.readline()
      while s:
        line = s.strip()
        state = self.lineLambda(state, line)
        s = f.readline()
      return self.summaryLambda(state)

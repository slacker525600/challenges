

def word_value(sWord):
  nToReturn = 0
  for cChar in sWord[1:-1]: #cutting off " marks
    nCharVal = ord(cChar) - ord('A') + 1
    if (nCharVal > 26 or nCharVal <= 0):
      print('error out of bounds')
    nToReturn += nCharVal
  return nToReturn #len(sWord) used as dummy when setting up function

def generate_triangles_to(nValue, anTriangles=[]):
  # can use anTriangles argument to say continue this list, as opposed to 
  if len(anTriangles) == 0:
    anTriangles.append(1)
  while anTriangles[-1] < nValue:
    anTriangles.append((len(anTriangles)+1)*(len(anTriangles)+2)/2)
  return anTriangles

#print(generate_triangles_to(15))

fFile = open('words.txt', 'r')
asLines = fFile.readlines()
fFile.close()

asWords = []
anTriangles = generate_triangles_to(55) #just starting somewhere. 
for sLine in asLines:
  asWords.extend(sLine.split(','))
#print(asWords)
#asWords = ['"SKY"'] #testing word val function matches expected value from example
nTriWordCount = 0
for sWord in asWords:
  nWordVal = word_value(sWord)
  #print(nWordVal)
  if anTriangles[-1] < nWordVal:
    anTriangles = generate_triangles_to(nWordVal, anTriangles)
  if nWordVal in anTriangles:
    nTriWordCount += 1
print(nTriWordCount)

def char_val(sToProc):
    nToReturn = 0 
    for cChar in sToProc:
        if cChar != '"':
            nToReturn += ord(cChar) - ord('A') + 1
    return nToReturn
print(char_val('COLIN'))
f = open('22.txt', 'r')
asNames = f.readlines()
f.close
asNames = asNames[0].split(',')

asNames.sort()
n = 1
nTotal = 0
while n < len(asNames) + 1:
    nTotal += n* char_val(asNames[n-1])
    if asNames[n-1] == '"COLIN"':
        print(n)
    n += 1
print (nTotal)

# just opening a file for starting...

def run():
  print("Hello world!")
  one()

def one():
  f = open('day1input.txt','r')
  s = f.readline()
  elfVal = 0
  elfTotals = []
  elfOn = 1
  while s:
    if len(s.strip())>0:
      elfVal = elfVal + int(s)
    else:
      elfOn = elfOn + 1
      elfTotals.append(elfVal)
      elfVal = 0
    s = f.readline()
  elfTotals.sort()

  print(sum(elfTotals[-3:]))

if __name__ == "__main__":
  run()
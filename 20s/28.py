#not sure Ill write any code for this, seems like a math problem 
#1 1
#3 1 + 3 + 5 + 7 + 9
#5 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25
#7 1 + 3 + 5 + 7 + 9 + ... + 31 + 37 + 43 + 49
#9 ... + 57 + 65 + 73 + 81
#so each expansion adds the next 4 in increments of the even number
def inc(n):
 return 4*n*n - (n-1)*6

nSum = 1
nCounter =1
while nCounter < 1001: #1001:
  nCounter += 2
  nSum += inc(nCounter)
print(nCounter, ":", nSum)

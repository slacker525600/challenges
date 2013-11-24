## what is so difficult about this problem, I tried to do it manually at first. 
#I must be missing something major here ... 
#tried to not write a program for this, but failed... bet I had some off by one issues? but  
#only 1-10 should have overlap ...  because those squares are in the table. 
#basically a 99-99 square 2-100 x 2-100
nSum = 99*99
#was doing it wrong
nSum += 9 #for first squares ... ie 2^2 is 4, but 4 isnt in there, 
#in fact this effect needs to be done for each first instance here, 
nSum += 3 + 2 +1 +1
for n in range(2,101):
  if   n%2 == 0:
    #all squares of 2(4), 3(9),4(16),5(25),6(36)...10(100)
    nSum -= 9
  elif n%3 == 0:
    # 2 3 4   and 9 for 27^2s
    nSum -= 4 
  elif n%4 == 0:
    #2 3 ... entirely captured by 2...
    print('should never reach here')
    nSum -= 2
  elif n%5 == 0:
    #just 2 ... and 8 and 4
    nSum -= 2
  elif n%6 ==0:
    nSum -= 1
    print('also should never get here')
  
  if n%5 == 0 and n%2 != 0: #dont double count, but ..., 15 would be excluded by 3 above mlrgh
    nSum -= 1 #8 -> 32
    # 16 would be each 4, but each 2 is already canceled to get 64

  if n%5 == 0: #16 to 32 and 64
    nSum -= 1
  elif n%3 == 0:
    nSum -= 1

  if  n%4 == 0:
    nSum -= 1 # just for 27... overlap with 81

  if n%6 == 0:
    nSum -= 1 #just for 32 overlap with 64

#print(nSum)

def i_will_see_this_later(n,exp):
  bToReturn = False
  if n == 2:
    if   exp%2 == 0 and exp != 2: #4 will not see 4 itself later
      bToReturn = True
    elif exp%3 == 0 and exp != 3: #8 
      bToReturn = True
    elif exp%4 == 0 : #and exp != 4: #16 # will see 16 later ... when 4^2 shows up
      print('should never get here')
    elif exp%5 == 0 and exp != 5: #32
      bToReturn = True
    elif exp%6 == 0 : #and exp != 6: #64 64 will show up as 8^2
      bToReturn = True
      print('should never get here')
  elif n == 3:
    if exp%2 == 0 and exp != 2: #9^x
      bToReturn = True
    elif exp%3 == 0 and exp != 3: #27^
      bToReturn = True
    elif exp%4 == 0: #81^x
      bToReturn = True
      print('should never get here')
  elif n == 4:
    if exp%2 == 0 and exp != 2: #16
      bToReturn = True
    elif exp%3 == 0 and exp != 3: # 64 ... 8^2 
      bToReturn = True
    elif exp%5 == 0: #32 4^5 = 32^2 so ... do get rid of it. 
      bToReturn = True
  elif n == 5:
    if exp%2 ==0 and exp != 2: #25
      bToReturn = True
  elif n == 6:
    if exp%2 == 0 and exp != 2: #36
      bToReturn = True
  elif n == 7:
    if exp%2 == 0 and exp != 2: #49
      bToReturn = True
  elif n == 8:
    # 3 .. 4 5 6 ... 
    if exp%2 == 0 and exp != 2: # 64
      bToReturn = True
    elif exp%4 == 0 and exp != 4: #16 
      print('should never reach here')
    elif exp%5 == 0 : # 32^3 = 8^5
      bToReturn = True 
  elif n == 9:
    if exp%2 == 0 and exp != 2: # 81
      bToReturn = True
    elif exp%3 == 0: #9^3 27^2
      bToReturn = True
  elif n == 10:
    if exp%2 == 0 and exp != 2: #100 ... 
      bToReturn = True
  elif n == 16:
    #16 has 4 factors of 2, so ... will overlap with 
    #32 every fifth and 64 every third. 5 , 6
    #this is a unique case where the third power will be excluded... 
    if exp%3 == 0: # 16^3 = 64^2
      bToReturn = True
    elif exp%5 == 0: # 16^5 = 32^4
      bToReturn = True
  elif n == 32:
    #32 has 5 2s so, will overlap with 64 at 32^6 == 64^5
    if exp%6 ==0:
      bToReturn = True
  elif n == 27:
    #27 has 3 3s, so 81^3 will equal 27^4
    if exp%4 == 0:
      bToReturn = True
  elif n == 64:
    bToReturn = False #same as 81 below, wont see anything higher
  elif n == 81:
    bToReturn = False # what 81 multiples will I see at a higher number
  return bToReturn


nSum = 99*99
nTotal =0
for n in [3,9,27,81]:#range(2,101)
  #[2,4,8,16,32,64]:
  nThisN = 0
  for exp in range(2,101):
    if i_will_see_this_later(n,exp):
      #print(n, exp)
      nSum -= 1
      nThisN +=1
    else:
      nTotal +=1
  #print('excluded ', nThisN, 'for', n)
#print(nSum, nTotal)
# frustrating
# 2
# 
# 


#going to try a different approach. 
#pfps, 
#row 2 
# deal with prime factors
# 2 4 8 16 32 64 
#2s 2-100 102 -200 201-300 304 - 400 402 - 500 504 - 600
nCount = 0
for n in range(2,601):
  if n%100 == 0:
    print(nCount)
  if n <= 100:
   nCount += 1
  elif n <= 200:
   if n%2==0 or n%3==0 or n%4==0 or n%5==0 or n%6==0:
     nCount += 1
  elif n <= 300:
   if n%3==0 or n%4==0 or n%5==0 or n%6==0:
     nCount += 1
  elif n <= 400:
   if n%4==0 or n%5==0 or n%6==0:
     nCount += 1
  elif n <= 500:
   if n%5==0 or n%6==0:
     nCount += 1
  elif n <= 600:
   if n%6==0:
     nCount += 1
  
#print(nCount)
nTwos = nCount 
# 3 9 27 81
nCount = 0
for n in range(2,401):
  if n%100 == 0:
    print(nCount)
  if n <= 100:
   nCount += 1
  elif n <= 200:
   if n%2==0 or n%3==0 or n%4==0:
     nCount += 1
  elif n <= 300:
   if n%3==0 or n%4==0:
     nCount += 1
  elif n <= 400:
   if n%4==0:
     nCount += 1
nThrees = nCount
#print(nCount)

# 7 49
# 6 36
# 5 25
# 10 100
#squares are each 50 + 99
# 99 * all the rest. 81
print(81*99 + 4*(50+99) + nTwos + nThrees)


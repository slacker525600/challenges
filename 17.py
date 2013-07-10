#!/usr/bin/python

def digit_rep(n):
    sToReturn = ''
    if (n == 1):
	sToReturn = 'One'
    elif (n ==2):
        sToReturn = 'Two'
    elif (n ==3):
        sToReturn = 'Three'
    elif (n ==4):
        sToReturn = 'four'
    elif (n ==5):
        sToReturn = 'five'
    elif (n ==6):
        sToReturn = 'six'
    elif (n ==7):
        sToReturn = 'seven'
    elif (n ==8):
        sToReturn = 'eight'
    elif (n ==9):
        sToReturn = 'nine'
    return sToReturn 

def digit_len(n):
    nToReturn = ''
    if (n == 1):
	nToReturn = 3
    elif (n ==2):
        nToReturn = 3 #'Two'
    elif (n ==3):
        nToReturn = 5 #'Three'
    elif (n ==4):
        nToReturn = 4 #'four'
    elif (n ==5):
        nToReturn = 4 #'five'
    elif (n ==6):
        nToReturn = 3 #'six'
    elif (n ==7):
        nToReturn = 5 #'seven'
    elif (n ==8):
        nToReturn = 5 #'eight'
    elif (n ==9):
        nToReturn = 4 # 'nine'
    return nToReturn 

def str_rep(n):
    sToReturn = ''
    if n == 1000:
        sToReturn = 'OneThousand'
    nHundreds = n/100
    sToReturn += digit_rep(nHundreds) + 'hundred'
    nRest = n%100
    if nRest != 0:
        sToReturn += 'and'
    return sToReturn

#print(str_rep(342))

#for n in range(1,1001):
#    if n == 1000:
#        print(n)


nAnswer = (3 + 3+ 5+4+4+3+5+5+4)*190 # one - 9
nAnswer += (3+6+6+8+8+7+7+9+8+8)*10 # ten - 19
nAnswer += (6+6+5+5+5+7+6+6)*100 #tens digits
nAnswer += (7) *900 #hundreds
nAnswer += 11 #1000
nAnswer += 3 * 99 * 9
print(nAnswer)
#groups for debugging sake
print('1-9')
print(3 + 3+ 5+4+4+3+5+5+4)
print('ten-19')
print(3+6+6+8+8+7+7+9+8+8)
print('tens digits')
print(6+6+5+5+5+7+6+6)

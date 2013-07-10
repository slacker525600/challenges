anMonthVals = [31,28,31,30,31,30,31,31,30,31,30,31]
sMonths = """jan feb mar apr3 may jun3 jul aug sep3 oct nov3 dec"""

nNumDaysTotal = 1 + 365 * 100 + 25
nOn = 1
nMonthOn = 0
nMonthSun = 0
while nOn < nNumDaysTotal:
    #if nOn > 6000:
    #    break
    print(nMonthOn, nMonthOn/12, (nMonthOn/12)%4)
    if (nMonthOn /12) %4 == 2 and nMonthOn%12 == 1:
        nOn += 29
        print('leap year')#nLeapYear)
    else:
        nOn += anMonthVals[nMonthOn%12]
    nMonthOn += 1
    if nOn % 7 == 0:
        nMonthSun += 1
        #print(nOn)
print(nMonthSun)
